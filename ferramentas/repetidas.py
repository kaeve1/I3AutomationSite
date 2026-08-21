# -*- coding: utf-8 -*-
"""A MESMA FOTOGRAFIA EM DOIS PAPEIS -- o que nao pode acontecer.

Cabecalho de pagina e fundo de secao sao papeis DIFERENTES: repetir a imagem
entre eles faz o visitante achar que voltou para uma pagina que ja viu. A
galeria e as placas de setor ficam de fora de proposito -- ali a repeticao e
esperada, porque a galeria e o acervo.

Achou, em 20/08, tres casos que ninguem tinha notado:

  cabecalho/servicos ... cabecalho de services E fundo em who-we-are
  faixa/refinaria ...... cabecalho de capabilities E fundo em who-we-are
  faixa/robotica ....... faixa da home E fundo de "The ledger"

Uso: python ferramentas/repetidas.py
"""
import re, io, glob, os
from collections import defaultdict

PAPEL = [
    ('cabecalho__foto', 'CABECALHO'),
    ('faixa__foto',     'faixa full-bleed'),
    ('dupla__foto',     'secao dupla'),
    ('secao__foto',     'fundo de secao'),
]

porpag = {}
uso = defaultdict(set)          # base -> {(pagina, papel)}
for f in sorted(glob.glob('site/*.html')):
    pag = os.path.basename(f).replace('.html', '')
    s = io.open(f, encoding='utf-8').read()
    linhas = []
    for m in re.finditer(r'<img\b[^>]*>', s):
        t = m.group(0)
        src = re.search(r'src="([^"]*)"', t)
        cls = re.search(r'class="([^"]*)"', t)
        if not src:
            continue
        base = re.sub(r'-\d+\.\w+$', '', src.group(1).replace('img/', ''))
        c = cls.group(1) if cls else ''
        papel = next((p for k, p in PAPEL if k in c), None)
        if papel is None:
            continue                      # galeria e placas: acervo, nao fundo
        linhas.append((papel, base))
        uso[base].add((pag, papel))
    porpag[pag] = linhas

print('=== fundos por pagina (galeria e placas de setor ficam de fora) ===')
for pag, linhas in porpag.items():
    if not linhas:
        continue
    print('  %s' % pag)
    for papel, base in linhas:
        print('     %-18s %s' % (papel, base))

print()
print('=== A MESMA FOTO EM MAIS DE UM LUGAR ===')
achou = False
for base, onde in sorted(uso.items()):
    if len(onde) > 1:
        achou = True
        print('  %-26s %s' % (base, ' | '.join('%s/%s' % o for o in sorted(onde))))
if not achou:
    print('  nenhuma')
