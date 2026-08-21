# -*- coding: utf-8 -*-
"""Auditoria de SEO do UnidoCLP, pagina a pagina, direto do ar."""
import re, urllib.request, ssl, html

BASE = 'https://universodoclp.pages.dev'
PAGS = ['/', '/quem-somos/', '/trabalhos-realizados/', '/treinamentos/', '/contato/']
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE

def pega(u):
    req = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=30, context=ctx).read().decode('utf-8','replace')

def um(s, pat):
    m = re.search(pat, s, re.I|re.S)
    return html.unescape(m.group(1).strip()) if m else None

print('%-24s %5s %5s %6s %6s %5s %5s %4s' % ('pagina','tit','desc','canon','og:img','ld+j','h1','lang'))
print('-'*72)
faltas = {}
for p in PAGS:
    s = pega(BASE+p)
    tit = um(s, r'<title[^>]*>(.*?)</title>')
    desc = um(s, r'name=["\']description["\'] content=["\'](.*?)["\']') or \
           um(s, r'content=["\'](.*?)["\'] name=["\']description["\']')
    canon = 'rel="canonical"' in s or "rel='canonical'" in s
    ogimg = len(re.findall(r'property=["\']og:image["\']', s, re.I))
    ld = len(re.findall(r'application/ld\+json', s, re.I))
    h1 = len(re.findall(r'<h1[ >]', s, re.I))
    lang = um(s, r'<html[^>]*lang=["\']([^"\']+)')
    print('%-24s %5s %5s %6s %6s %5d %5d %4s' % (
        p, len(tit or ''), len(desc or ''), 'sim' if canon else 'NAO',
        ogimg or 'NAO', ld, h1, lang or '?'))
    for k, v in (('description', desc), ('canonical', canon), ('og:image', ogimg), ('ld+json', ld)):
        if not v: faltas.setdefault(k, []).append(p)

print()
print('=== falta em quais paginas ===')
for k, v in faltas.items():
    print('  %-12s %d de 5  %s' % (k, len(v), '(todas)' if len(v)==5 else ' '.join(v)))

print()
print('=== global ===')
s = pega(BASE+'/')
for nome, pat in [('favicon svg', r'rel=["\']icon["\'][^>]*svg'),
                  ('favicon ico', r'favicon\.ico'),
                  ('apple-touch-icon', r'apple-touch-icon'),
                  ('manifest', r'rel=["\']manifest["\']'),
                  ('theme-color', r'name=["\']theme-color["\']'),
                  ('twitter:card', r'twitter:card'),
                  ('og:type', r'og:type'),
                  ('preload da fonte', r'rel=["\']preload["\'][^>]*font'),
                  ('script de terceiro', r'<script[^>]+src=["\']https?://(?!universodoclp)')]:
    print('  %-20s %s' % (nome, 'sim' if re.search(pat, s, re.I) else 'NAO'))
imgs = re.findall(r'<img\b[^>]*>', s)
print('  %-20s %d de %d' % ('imgs com alt', sum(1 for i in imgs if 'alt=' in i), len(imgs)))
print('  %-20s %s' % ('formatos', ' '.join(sorted(set(re.findall(r'\.(avif|webp|jpg|png)', s))))))
