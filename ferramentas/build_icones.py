# -*- coding: utf-8 -*-
"""Gera a familia de icones a partir do UNICO favicon.svg.

Por que existe, se ja havia um favicon: o SVG sozinho nao cobre tres casos
reais, e nenhum deles da erro visivel -- o icone simplesmente nao aparece.

  1. O navegador pede `/favicon.ico` SOZINHO, sem link nenhum no HTML, e o
     buscador olha para la. Sem o arquivo sao 404 em toda visita.
  2. `apple-touch-icon` em SVG e IGNORADO pelo iOS. Quem salva o site na tela
     inicial do iPhone recebe um retrato da pagina, nao a marca.
  3. Sem manifesto, o Android usa o favicon de 32px ampliado no atalho.

O SVG continua sendo a FONTE: os rasteres saem dele, por captura no Chrome,
e nao de um desenho paralelo em PIL. Redesenhar o "3" com primitivas seria a
terceira copia do glifo -- a mesma armadilha que `icone_marca()` documenta e
que marca.js evita lendo a geometria do DOM.
"""
import io
import json
import os
import subprocess
import sys

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(RAIZ, 'site')
SVG = os.path.join(SITE, 'brand', 'favicon.svg')

# As larguras nao sao gosto. Cada uma tem um consumidor nomeado:
#   16/32/48 -> dentro do .ico (aba, favoritos, e o que o Google mostra)
#   180 ..... -> apple-touch-icon, o tamanho que o iOS pede desde o iPhone 6+
#   192/512 . -> manifesto do Android; 512 e o minimo para o splash
PNGS = [180, 192, 512]
ICO = [16, 32, 48]


def rasterizar(tamanhos):
    """Captura o SVG no Chrome, um tamanho por vez. Devolve {tam: PIL.Image}."""
    script = os.path.join(os.path.dirname(__file__), 'velocidade', '_icones.mjs')
    with open(script, 'w', encoding='utf-8') as f:
        f.write(_JS % json.dumps(sorted(set(tamanhos))))
    saida = subprocess.run([_node(), script, SVG], capture_output=True, text=True)
    if saida.returncode:
        raise SystemExit('captura falhou:\n' + saida.stderr)
    dados = json.loads(saida.stdout)
    import base64
    return {int(k): Image.open(io.BytesIO(base64.b64decode(v))).convert('RGBA')
            for k, v in dados.items()}


def _node():
    return 'node'


_JS = r'''
import { abrirChrome, fecharChrome, Sessao } from "../movel/cdp.mjs";
import { readFileSync } from "node:fs";
const TAMANHOS = %s;
const svg = readFileSync(process.argv[2], "utf8");
const ch = await abrirChrome(9406);
const b = await Sessao.conectar(ch.browserWs);
const { targetId } = await b.enviar("Target.createTarget", { url: "about:blank" });
const { sessionId } = await b.enviar("Target.attachToTarget", { targetId, flatten: true });
const s = (m, p) => b.enviar(m, p, sessionId);
await s("Page.enable"); await s("Runtime.enable");
const saida = {};
for (const t of TAMANHOS) {
  await s("Emulation.setDeviceMetricsOverride", { width: t, height: t, deviceScaleFactor: 1, mobile: false });
  // O SVG vai INLINE no documento, sem margem e sem fundo do navegador: um
  // <img src=...> herdaria o branco da pagina nas bordas antisserrilhadas.
  const doc = `<!doctype html><meta charset=utf-8><style>
    html,body{margin:0;padding:0;width:${t}px;height:${t}px;overflow:hidden;background:transparent}
    svg{display:block;width:${t}px;height:${t}px}</style>` + svg;
  await s("Page.navigate", { url: "data:text/html;charset=utf-8," + encodeURIComponent(doc) });
  await new Promise(r => setTimeout(r, 250));
  const { data } = await s("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
  saida[t] = data;
}
console.log(JSON.stringify(saida));
b.fechar(); fecharChrome(ch);
'''


def main():
    if not os.path.exists(SVG):
        raise SystemExit('nao achei ' + SVG)
    imagens = rasterizar(PNGS + ICO)
    rel = []

    for t in PNGS:
        nome = ('apple-touch-icon.png' if t == 180 else 'icon-%d.png' % t)
        p = os.path.join(SITE, 'brand', nome)
        # Achatado sobre o navy da marca: o iOS nao respeita alfa no atalho e
        # compoe sobre PRETO, o que engrossaria a moldura do monitor.
        chapa = Image.new('RGB', (t, t), (0, 53, 102))
        chapa.paste(imagens[t], (0, 0), imagens[t])
        chapa.save(p, optimize=True)
        rel.append((os.path.relpath(p, RAIZ), os.path.getsize(p)))

    # O .ico vai na RAIZ do site, nao em brand/: o pedido automatico do
    # navegador e para `/favicon.ico` e nao passa por link nenhum do HTML.
    p = os.path.join(SITE, 'favicon.ico')
    imagens[max(ICO)].save(p, format='ICO',
                           sizes=[(t, t) for t in sorted(ICO)])
    rel.append((os.path.relpath(p, RAIZ), os.path.getsize(p)))

    manifesto = {
        'name': 'i3 Automations & Controls',
        'short_name': 'i3Automations',
        'start_url': '.',
        'display': 'browser',
        'background_color': '#001D3D',
        'theme_color': '#003566',
        'icons': [
            {'src': 'brand/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
            {'src': 'brand/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
            {'src': 'brand/favicon.svg', 'sizes': 'any', 'type': 'image/svg+xml'},
        ],
    }
    p = os.path.join(SITE, 'site.webmanifest')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(manifesto, f, indent=2)
    rel.append((os.path.relpath(p, RAIZ), os.path.getsize(p)))

    print('== icones ==')
    for nome, tam in rel:
        print('   %-34s %6.1f KB' % (nome, tam / 1024))
    print('   TOTAL %.1f KB' % (sum(t for _, t in rel) / 1024))


if __name__ == '__main__':
    main()
