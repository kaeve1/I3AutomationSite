# -*- coding: utf-8 -*-
"""Publica CSS e JS: da FONTE comentada para o `site/` enxuto.

POR QUE ISTO EXISTE, e a decisao vale mais que o codigo.

O usuario pediu para "retirar todos os comentarios do codigo". O ganho e real
-- 49% do CSS+JS deste site sao comentario, 195 KB. Mas apagar da FONTE
contradiz a regra critica no3 do CLAUDE.md: "se um numero entrar no CSS, tem
que existir a conta que o produziu". Sao 88 medicoes so no style.css: cada
contraste WCAG, cada proporcao conferida, cada armadilha que custou uma sessao.

Entao a separacao: a fonte fica em `fonte/`, comentada; o `site/` recebe a
versao publicada, sem comentario. O deploy continua sendo "publicar a pasta
site/" -- este script roda na AUTORIA, junto com build_site.py, exatamente
como o gerador de paginas ja fazia.

O QUE ELE NAO FAZ, de proposito: nao renomeia variavel, nao reordena regra,
nao junta seletor, nao remove ponto-e-virgula. Minificador agressivo troca
bytes por risco, e este site nao tem teste automatizado que pegue uma
regressao dessas. O que sai e o que e SEGURO tirar: comentario, indentacao e
linha em branco.

A ARMADILHA DO STRIPPER DE JS, que e o motivo de ele nao ser um regex de tres
linhas: `//` aparece dentro de string -- `"https://i3automations.com"` -- e
dentro de expressao regular. Um stripper ingenuo come a URL inteira a partir
do `//` e o arquivo continua com sintaxe valida, entao nem o `node --check`
acusa. Por isso aqui ha uma maquina de estados que sabe onde esta: string
simples, dupla, template, regex ou codigo.

Uso: python ferramentas/build_ativos.py
"""
import os
import re
import shutil

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RAIZ, 'fonte')
DEST = os.path.join(RAIZ, 'site')


def tirar_comentarios_js(src):
    """Remove comentarios de JS respeitando string, template e regex.

    Devolve (saida, literais) -- a lista de literais serve de PROVA: se um
    deles mudou, o stripper comeu conteudo em vez de comentario.
    """
    out = []
    literais = []
    i, n = 0, len(src)
    # o ultimo token significativo decide se `/` abre regex ou e divisao
    anterior = ''
    while i < n:
        c = src[i]
        d = src[i:i + 2]

        if d == '//':
            j = src.find('\n', i)
            i = n if j < 0 else j
            continue
        if d == '/*':
            j = src.find('*/', i + 2)
            i = n if j < 0 else j + 2
            # comentario entre tokens vira espaco, senao `a/*x*/b` colaria
            out.append(' ')
            continue

        if c in '"\'`':
            fim = c
            j = i + 1
            while j < n:
                if src[j] == '\\':
                    j += 2
                    continue
                if src[j] == fim:
                    break
                j += 1
            lit = src[i:j + 1]
            out.append(lit)
            literais.append(lit)
            anterior = 'lit'
            i = j + 1
            continue

        if c == '/' and anterior not in ('ident', ')', ']', 'lit'):
            # expressao regular: consome ate a barra de fecho, pulando classes
            j = i + 1
            classe = False
            while j < n:
                if src[j] == '\\':
                    j += 2
                    continue
                if src[j] == '[':
                    classe = True
                elif src[j] == ']':
                    classe = False
                elif src[j] == '/' and not classe:
                    break
                elif src[j] == '\n':
                    break
                j += 1
            out.append(src[i:j + 1])
            anterior = 'lit'
            i = j + 1
            continue

        out.append(c)
        if c.isalnum() or c in '_$':
            anterior = 'ident'
        elif c in ')]':
            anterior = c
        elif not c.isspace():
            anterior = c
        i += 1
    return ''.join(out), literais


def enxugar(txt):
    """Tira indentacao e linha em branco, preservando o resto verbatim.

    NAO colapsa espacos dentro da linha: `calc(100% - 20px)` PRECISA dos
    espacos em volta do `-`, e um minificador que os remove quebra o calc sem
    erro nenhum -- o valor simplesmente vira invalido e a declaracao cai.
    """
    linhas = []
    for ln in txt.split('\n'):
        ln = ln.rstrip()
        if not ln.strip():
            continue
        linhas.append(ln.strip())
    return '\n'.join(linhas) + '\n'


def publicar():
    rel = []
    for sub, ext in (('css', '.css'), ('js', '.js')):
        origem = os.path.join(FONTE, sub)
        destino = os.path.join(DEST, sub)
        if not os.path.isdir(origem):
            continue
        os.makedirs(destino, exist_ok=True)
        for nome in sorted(os.listdir(origem)):
            if not nome.endswith(ext):
                continue
            with open(os.path.join(origem, nome), encoding='utf-8') as fh:
                src = fh.read()
            antes = len(src.encode('utf-8'))

            if ext == '.js':
                saida, lit_antes = tirar_comentarios_js(src)
                _, lit_depois = tirar_comentarios_js(saida)
                # PROVA: nenhum literal pode ter mudado. Se mudou, o stripper
                # comeu conteudo -- e conteudo comido continua compilando.
                assert lit_antes == lit_depois, \
                    '%s: literal alterado pelo stripper' % nome
            else:
                saida = re.sub(r'/\*.*?\*/', '', src, flags=re.S)

            saida = enxugar(saida)
            # A UNICA LINHA DE COMENTARIO QUE SOBREVIVE, e ela paga o proprio
            # peso: sem ela, alguem abre `site/css/style.css`, edita, e o
            # proximo build APAGA o trabalho sem dizer nada. 60 bytes contra
            # uma tarde perdida.
            banner = ('/* GERADO por ferramentas/build_ativos.py'
                      ' -- edite fonte/%s */' % (sub + '/' + nome))
            saida = banner + chr(10) + saida
            with open(os.path.join(destino, nome), 'w', encoding='utf-8') as fh:
                fh.write(saida)
            depois = len(saida.encode('utf-8'))
            rel.append((sub + '/' + nome, antes, depois))
    return rel


def main():
    if not os.path.isdir(FONTE):
        raise SystemExit('fonte/ nao existe -- nada a publicar')
    rel = publicar()
    print('== ativos publicados (fonte/ -> site/) ==')
    ta = td = 0
    for nome, a, d in rel:
        ta += a
        td += d
        print('   %-22s %7.1fK -> %6.1fK   -%2.0f%%'
              % (nome, a / 1024, d / 1024, 100 * (a - d) / a))
    print('   %-22s %7.1fK -> %6.1fK   -%2.0f%%'
          % ('TOTAL', ta / 1024, td / 1024, 100 * (ta - td) / ta))


if __name__ == '__main__':
    main()
