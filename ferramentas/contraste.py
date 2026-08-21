# -*- coding: utf-8 -*-
"""Contraste WCAG 2.1 dos pares que o site usa de verdade.

Regra do projeto (CLAUDE.md #3): se um numero entra no CSS, existe a conta que
o produziu. Este arquivo E a conta. Rodar de novo apos qualquer mexida em cor.

Uso: python ferramentas/contraste.py
"""


def canal(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def razao(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def sobre(fundo, fg, alfa):
    """Achata uma cor com alfa sobre o fundo — rgba nao tem contraste sozinho."""
    f = [int(fundo.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    c = [int(fg.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    m = [round(cc * alfa + ff * (1 - alfa)) for cc, ff in zip(c, f)]
    return '#%02X%02X%02X' % tuple(m)


CLARO = {
    'sup-1': '#FFFFFF', 'sup-2': '#F2F5F8', 'sup-3': '#001D3D',
    'tinta': '#1A1A1A', 'tinta-2': '#40607F', 'tinta-suave': '#5A5A5A',
    'navy': '#003566', 'dourado': '#FDC500', 'dourado-txt': '#6B5000',
    'navy-luz': '#8FB4DC',
}

ESCURO = {
    'sup-1': '#000C18', 'sup-2': '#001427', 'sup-3': '#003566',
    'tinta': '#E8EDF3', 'tinta-2': '#9FBEE0', 'tinta-suave': '#A8BACB',
    'dourado': '#FDC500', 'navy-luz': '#8FB4DC',
}

# (rotulo, texto, fundo, minimo exigido)
PARES = [
    ('CLARO  corpo sobre branco', CLARO['tinta'], CLARO['sup-1'], 4.5),
    ('CLARO  corpo sobre off-white', CLARO['tinta'], CLARO['sup-2'], 4.5),
    ('CLARO  eyebrow sobre branco', CLARO['tinta-2'], CLARO['sup-1'], 4.5),
    ('CLARO  eyebrow sobre off-white', CLARO['tinta-2'], CLARO['sup-2'], 4.5),
    ('CLARO  legenda sobre branco', CLARO['tinta-suave'], CLARO['sup-1'], 4.5),
    ('CLARO  titulo navy sobre branco', CLARO['navy'], CLARO['sup-1'], 4.5),
    ('CLARO  titulo navy sobre off-white', CLARO['navy'], CLARO['sup-2'], 4.5),
    ('CLARO  dourado-txt sobre branco', CLARO['dourado-txt'], CLARO['sup-1'], 4.5),
    ('CLARO  dourado-txt sobre off-white', CLARO['dourado-txt'], CLARO['sup-2'], 4.5),
    ('CLARO  branco sobre bloco navy', '#FFFFFF', CLARO['sup-3'], 4.5),
    ('CLARO  paragrafo .72 sobre navy', sobre(CLARO['sup-3'], '#FFFFFF', .72), CLARO['sup-3'], 4.5),
    ('CLARO  dourado sobre bloco navy', CLARO['dourado'], CLARO['sup-3'], 3.0),
    ('CLARO  link claro sobre navy', CLARO['navy-luz'], CLARO['sup-3'], 4.5),
    ('CLARO  ALERTA dourado sobre branco', CLARO['dourado'], CLARO['sup-1'], 4.5),
    ('ESCURO corpo sobre sup-1', ESCURO['tinta'], ESCURO['sup-1'], 4.5),
    ('ESCURO corpo sobre sup-2', ESCURO['tinta'], ESCURO['sup-2'], 4.5),
    ('ESCURO corpo sobre sup-3', ESCURO['tinta'], ESCURO['sup-3'], 4.5),
    ('ESCURO eyebrow sobre sup-1', ESCURO['tinta-2'], ESCURO['sup-1'], 4.5),
    ('ESCURO eyebrow sobre sup-2', ESCURO['tinta-2'], ESCURO['sup-2'], 4.5),
    ('ESCURO eyebrow sobre sup-3', ESCURO['tinta-2'], ESCURO['sup-3'], 4.5),
    ('ESCURO legenda sobre sup-1', ESCURO['tinta-suave'], ESCURO['sup-1'], 4.5),
    ('ESCURO legenda sobre sup-2', ESCURO['tinta-suave'], ESCURO['sup-2'], 4.5),
    ('ESCURO dourado sobre sup-1', ESCURO['dourado'], ESCURO['sup-1'], 4.5),
    ('ESCURO dourado sobre sup-2', ESCURO['dourado'], ESCURO['sup-2'], 4.5),
    ('ESCURO dourado sobre sup-3', ESCURO['dourado'], ESCURO['sup-3'], 3.0),
    ('ESCURO paragrafo .74 sobre sup-1', sobre(ESCURO['sup-1'], '#E8EDF3', .74), ESCURO['sup-1'], 4.5),
    ('ESCURO paragrafo .74 sobre sup-3', sobre(ESCURO['sup-3'], '#E8EDF3', .74), ESCURO['sup-3'], 4.5),
    ('ESCURO navy-luz sobre sup-1', ESCURO['navy-luz'], ESCURO['sup-1'], 4.5),
]

# Bordas e reguas: alvo 3:1 (componente nao-textual, WCAG 1.4.11)
BORDAS = [
    ('CLARO  borda .15 sobre branco', sobre('#FFFFFF', '#000000', .15), '#FFFFFF', 3.0),
    ('CLARO  borda .22 sobre branco', sobre('#FFFFFF', '#000000', .22), '#FFFFFF', 3.0),
    ('CLARO  borda .28 sobre off-white', sobre('#F2F5F8', '#000000', .28), '#F2F5F8', 3.0),
    ('ESCURO borda .18 sobre sup-1', sobre('#000C18', '#FFFFFF', .18), '#000C18', 3.0),
    ('ESCURO borda .26 sobre sup-1', sobre('#000C18', '#FFFFFF', .26), '#000C18', 3.0),
    ('ESCURO borda .26 sobre sup-2', sobre('#001427', '#FFFFFF', .26), '#001427', 3.0),
]


def tabela(titulo, pares):
    print('\n%s' % titulo)
    print('-' * 74)
    falhas = 0
    for rotulo, fg, bg, minimo in pares:
        r = razao(fg, bg)
        ok = r >= minimo
        if not ok:
            falhas += 1
        print('%-42s %6.2f:1  min %.1f  %s' % (rotulo, r, minimo, 'ok' if ok else 'FALHA'))
    return falhas


if __name__ == '__main__':
    f = tabela('TEXTO', PARES)
    f += tabela('BORDAS E REGUAS (nao-textual, 3:1)', BORDAS)
    print('\n%d falha(s).' % f)
    print('Nota: a linha ALERTA e intencional — prova que #FDC500 nao serve')
    print('de texto sobre claro. E por isso que --dourado-txt existe.')
