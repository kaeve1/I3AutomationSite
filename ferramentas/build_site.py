# -*- coding: utf-8 -*-
"""Conteudo das nove paginas do site i3Automations.

build_paginas.py tem o CHROME (nav, rodape, cabecalho, componentes repetidos);
este arquivo tem o CONTEUDO. A separacao existe porque as duas coisas mudam por
motivos diferentes: o chrome muda quando o sistema de design muda, o conteudo
muda quando o cliente tem novidade.

TOM DE VOZ (design.md §4). O site atual do cliente esta escrito em jargao de
marketing — "revolutionize", "cutting-edge", "game-changing", "unparalleled".
O §4.1 proibe todos. O FATO de cada frase foi preservado; a EMBALAGEM foi
refeita em registro declarativo, primeira pessoa do plural, prova antes de
promessa. Nenhum numero, nome de cliente ou credencial foi inventado: tudo o
que esta aqui veio do site atual ou de memoria.md.

Uso: python ferramentas/build_site.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_paginas import (
    pagina, cabecalho, cta, imagem, icone_marca, marca_3d, lente, lista_capacidades,
    grade_plataformas, grade_setores, prancha, registro_obras, oferta, contratos, feixe,
    diagrama,
    secao_com_foto, NUMEROS, peca, cota_peca, sitemap, robots, cabecalhos_deploy,
    redirecionamentos_deploy, htaccess_deploy,
    GOVERNO,
    CONTATO_CTA, TEL_VENDAS, TEL_SUPORTE, EMAIL, WHATSAPP, REDES, DEST,
)



# ----------------------------------------------------------------- BRACO
#  O robo de 6 eixos do heroi. Nao carrega imagem: a geometria e gerada em
#  js/braco.js a partir de circulos, e as juntas se movem por cinematica
#  direta na GPU. O <div> estatico so aparece quando nao ha WebGL2 -- e ai
#  ele usa a mascara de traco do MESMO braco, para o desenho ser o mesmo.
BRACO = (
    '<div class="braco" data-braco role="img" '
    'aria-label="Interactive line drawing of a six-axis industrial robot arm '
    'at work: drag to orbit it, and the pointer lights the drawing in gold.">'
    '<canvas class="braco__tela"></canvas>'
    '<div class="braco__estatico" aria-hidden="true"></div>'
    '</div>'
)

# =========================================================================
#  HOME
#  A estrutura varia de proposito em relacao ao UnidoCLP (pedido do usuario):
#  as competencias deixam de ser grade de cards e viram lista numerada de
#  largura total, com regua que se preenche — le como sumario de caderno
#  tecnico; e entra um bloco que la nao existe, a planta isometrica navegavel.
# =========================================================================
def home():
    corpo = '''
<section class="heroi reticula" id="top">
  <div class="heroi__container">
    <!-- A peca vive DENTRO da grade, na mesma linha do texto: e o unico jeito
         de ela ficar centralizada com o texto em qualquer altura de janela.
         Absoluta no heroi, ela ficava presa ao fundo da secao. -->
    <div class="heroi__peca">%(braco)s</div>
    <div class="heroi__texto">
      <p class="heroi__marca">%(marca)s<span>Automations<br>&amp; Controls</span></p>
      <h1 class="heroi__titulo">
        <span class="entra-linha" style="--i:0"><span class="realce">Good control strategy</span></span>
        <span class="entra-linha" data-lente-texto style="--i:1">beats more expensive</span>
        <span class="entra-linha" data-lente-texto style="--i:2">instrumentation.</span>
      </h1>
      <p class="heroi__apoio" data-lente-texto>Control panels, PLC and SCADA integration, instrumentation
      and commissioning. Lakewood Ranch, Florida &mdash; in the field since 2000.</p>
    </div>

    <div class="heroi__rodape">
      <span>Industrial automation integration</span>
      <span>Federal contractor &middot; UEI <span class="mono">XUZ4WKEZLS67</span></span>
      <span class="heroi__dica">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.4a8.6 8.6 0 0 1 8.6 8.6M12 20.6A8.6 8.6 0 0 1 3.4 12"/><path d="M18.5 2.6L20.9 5l-2.4 2.4M5.5 21.4L3.1 19l2.4-2.4"/></svg>
        Drag the arm to orbit &middot; the pointer lights the drawing
      </span>
    </div>
  </div>
</section>

<section class="secao" id="who-we-are">
  <div class="container">
    <div class="bloco bloco--centro reveal">
      <!-- O REALCE DOURADO MUDOU DE LINHA, a pedido: ele estava na tese
           ("We build the control system") e o pedido era que marcasse "What we
           actually do".

           E a colocacao certa, e nao so porque foi pedida. O realce e um
           MARCADOR -- ele aponta onde o capitulo comeca, do mesmo jeito que a
           faixa da headline aponta a tese da empresa na dobra de cima. Sobre a
           lead ele competia com o h1 do heroi: duas frases longas em campo
           dourado na mesma rolagem leem como duas manchetes. Sobre o rotulo da
           secao ele vira o que sempre foi, uma aba de capitulo.

           O par de cor nao muda e nao precisa de medicao nova: navy #003566
           sobre campo `--dourado`, 7,74:1, opaco. E a contagem de dourado da
           dobra CAI de dois para um -- a lead volta a ser texto. -->
      <p class="eyebrow"><span class="realce">What we actually do</span></p>
      <div>
        <p class="lead">We build the control system and hand
        you the plant that runs it &mdash; panel, code, network, and drawings that match
        the wall.</p>

        <div class="pilha" style="margin-top: var(--s-5)">
          <p>i3 Automations &amp; Controls has been integrating industrial control systems
          since 2000. Control panels, PLC and SCADA programming, instrumentation,
          commissioning. Oil and gas in Houston, water and wastewater across Florida,
          automotive body shops, paper mills, and utility-scale solar.</p>
          <p>We are a registered federal contractor, certified on Ignition, VTScada and
          Canary. The work is the same either way: understand the process, choose the
          strategy that fits it, and leave behind a system the plant staff can run without
          calling us.</p>
        </div>

        %(cta)s
      </div>
    </div>
    %(prancha)s
    %(numeros)s
  </div>
</section>

<section class="secao secao--offwhite" id="capabilities">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Capabilities</p>
        <h2>Eight disciplines, <br>one contractor</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Most plants end up coordinating a panel shop, a programmer, an
        instrument tech and a commissioning crew &mdash; and owning every gap between them.
        We carry all four, which is why the drawings match the code and the code matches
        what is wired.</p>
        %(cta_cap)s
      </div>
    </div>
    %(capacidades)s
  </div>
</section>

<section class="faixa reveal reveal--limpo">
  %(faixa)s
  <div class="container">
    <p class="eyebrow reveal">From strategy to startup</p>
    <h2 class="reveal" style="--i:1">The panel leaves our shop already tested</h2>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Platforms we run</p>
        <h2>The stack the <br>process needs</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">We are certified on three SCADA platforms and fluent on three PLC
        families. Which one a project uses is a decision about the process, the plant's
        existing standard, and who has to maintain it after we leave &mdash; never about
        what we would rather write.</p>
      </div>
    </div>
    %(plataformas)s
  </div>
</section>

<section class="secao secao--offwhite" id="plant">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">How a plant reaches the control room</p>
        <h2>Every asset, <br>one supervision layer</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">This is the topology behind every project on this page: field
        assets on the outside, a supervision layer in the middle, and a documented path
        between them. Drag to walk around it; the pointer lights what it crosses.</p>
      </div>
    </div>

    <div class="planta reveal" data-planta role="img"
         aria-label="Interactive isometric drawing of an industrial plant: field assets connected by documented links to a central control room.">
      <canvas class="planta__tela"></canvas>
      <div class="planta__grade" aria-hidden="true"></div>
      <p class="planta__dica">DRAG TO ORBIT &middot; POINTER LIGHTS THE DRAWING</p>
      <p class="planta__legenda">
        <span>Control room &middot; SCADA</span><span>Oil &amp; Gas</span><span>Water</span>
        <span>Automotive</span><span>Paper</span><span>Solar</span><span>MCC</span>
      </p>
      <p class="planta__semwebgl">This drawing needs WebGL2, which this browser has turned
      off. The plants themselves are on the <a class="link"
      href="past-performance.html">past performance</a> page.</p>
    </div>
  </div>
</section>

<section class="secao" id="industries">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Industries served</p>
        <h2>Where our <br>controls run</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Five sectors, one discipline. What changes between a refinery and
        a body shop is the process and the consequence of getting it wrong &mdash; not the
        rigor the control system deserves.</p>
      </div>
    </div>
    %(setores)s
  </div>
</section>

<div class="dupla">
  %(foto_dupla)s
<section class="secao secao--escura secao--compacta">
  <div class="container">
    <div class="bloco bloco--centro reveal">
      <p class="eyebrow">Why the call is worth making</p>
      <p class="citacao">Senior control experts know things they do not teach in
      school.</p>
    </div>
  </div>
</section>

%(contato)s
</div>
''' % {
        # A peça do herói deixou de ser fotografia. É geometria gerada em
        # js/braco.js — mesma técnica da planta, outra escala de olhar. Sem
        # imagem no caminho crítico: o LCP do herói passou a ser a headline.
        'braco': BRACO,
        # `data-intro-destino` e o alvo do voo da intro, e `data-encaixe` fica
        # em 1: a marca pousa exatamente sobre si mesma, mesmo desenho e mesma
        # proporcao, o que o par foto/traco do braco nunca conseguiu.
        'marca': icone_marca('heroi__icone',
                             extra=' data-intro-destino data-encaixe="1"'),
        'cta': cta('who-we-are.html', 'Who we are'),
        'cta_cap': cta('capabilities.html', 'All capabilities'),
        'numeros': NUMEROS,
        'capacidades': lista_capacidades(),
        'faixa': imagem('faixa/robotica', [1280, 1920],
                        'Robotic handling cell in a distribution facility',
                        '100vw', classe='faixa__foto'),
        'plataformas': grade_plataformas(),
        'setores': grade_setores(),
        # O bloco de credenciais federais saiu da home e das outras páginas: ele
        # vive SÓ em who-we-are agora, que é onde o comprador público procura
        # perfil de fornecedor. Repetido em quatro páginas ele competia com o
        # assunto de cada uma — e a fotografia de refinaria foi junto para lá.
        # O CTA perde a foto PROPRIA: quem carrega a fotografia agora e o
        # invólucro `.dupla`, uma imagem so para as duas secoes.
        'contato': CONTATO_CTA,
        'foto_dupla': imagem(
            'dupla/clp', [1280, 1920, 2560],
            'Open control panel with PLC racks, breakers and terminal blocks',
            '100vw', classe='dupla__foto'),
        # As quatro sao fotografia AUTORAL de campo, entregue pelo cliente —
        # nenhuma e banco de imagem, que e a preferencia absoluta do §6.5.
        'prancha': prancha([
            ('galeria/scada', [600],
             'SCADA screen showing effluent station discharge flow, with an '
             'i3Automations hard hat in the foreground',
             'SCADA',
             'Effluent station discharge flow, on shift'),
            ('galeria/painel-campo', [600],
             'Field-installed control panel with pilot lights and selector '
             'switches, door open at a pump station',
             'CONTROL PANEL',
             'Pump station, door open for commissioning'),
            ('galeria/bomba', [600],
             'Submersible pump set being lowered by crane into a wet well',
             'INSTRUMENTATION',
             'Submersible set going into the wet well'),
            ('galeria/obra-agua', [600],
             'Controls cabinet being installed beside weir gates at a water '
             'treatment structure under construction',
             'FIELD BUILD',
             'Weir gate structure, controls going in'),
        ], 'WATER &middot; WASTEWATER &middot; PANEL SHOP &middot; SUPERVISION'),
        'pp_body_in_white': imagem('galeria/body-in-white', [600], 'Robotic welding line in an automotive body shop', '(max-width: 700px) 92vw, 132px'),
        'pp_celula': imagem('galeria/celula', [400, 800], 'Robotic cell on an automotive production line', '(max-width: 700px) 92vw, 132px'),
        'pp_comissionamento': imagem('galeria/comissionamento', [600], 'Engineer commissioning a control system at a command station', '(max-width: 700px) 92vw, 132px'),
        'pp_captacao': imagem('galeria/captacao', [600], 'Large-diameter pipework at a water intake station', '(max-width: 700px) 92vw, 132px'),
        'pp_solar': imagem('setores/solar', [336, 672], 'Utility-scale photovoltaic array', '(max-width: 700px) 92vw, 132px'),
    }
    return pagina(
        'index.html',
        'i3Automations &mdash; Industrial Control Panels, PLC and SCADA',
        'Control panels, PLC and SCADA programming, instrumentation and commissioning '
        'for oil and gas, water, automotive and solar. Federal contractor since 2000.',
        corpo, sobre_heroi=True, intro=True,
        # o braço é só o herói; os cinco cards de setor continuam sendo lentes
        scripts_extra=('braco.js', 'lente.js', 'planta.js'))


# ============================================================ WHO WE ARE
def quem_somos():
    # Os tres trechos da rota. As coordenadas sao percentuais do trecho, e o x
    # salta entre 6 e 14 para a linha DESCER EM DEGRAUS -- e o cotovelo em
    # angulo reto que faz ler como eletrocalha, nao como grafico.
    #
    # Vive numa variavel, e nao inline no `%`, porque o corpo desta pagina e
    # feito de DOIS literais concatenados (NUMEROS entra no meio). Um `%` no fim
    # so alcanca o ultimo literal -- foi assim que o primeiro trecho saiu como
    # `%(feixe_1)s` cru no HTML.
    # Os tres trechos do feixe. Todo trecho comeca e termina nos mesmos
    # quatro x, entao a emenda entre secoes fecha sem calculo nenhum.
    feixes = {
        # O barramento entra pela esquerda, cruza para a direita na seção dos
        # números, corre à direita na missão, e volta para a esquerda no método.
        'feixe_1': feixe('esq', 'dir'),
        'feixe_3': feixe('dir', 'esq'),
    }
    # A secao "Since 2000" NAO tem mais foto de fundo (19/08, a pedido do
    # usuario). O `foto_desde` que morava aqui saiu junto -- ver a nota na
    # marcacao da secao, logo abaixo.
    extras = {
        # NAO `cabecalho/servicos`: aquela e o CABECALHO de services, e a mesma
        # foto em dois papeis foi o que a auditoria de 20/08 proibiu.
        # `faixa/prensa` e a de maior amplitude do acervo sob o veu navy (63,5)
        # -- e a amplitude que faz uma foto sobreviver a camada que a cobre.
        'foto_missao': imagem('faixa/ferramental', [1280, 1920, 2560],
                              'Tooling and guide pillars under an industrial press',
                              '100vw', classe='secao__foto'),
        'diagrama': diagrama([
            ('01', 'Understand the process',
             'P&amp;IDs, existing logic, and a conversation with whoever runs the '
             'plant at night. The constraints are rarely in the drawings.'),
            ('02', 'Choose the strategy',
             'Control philosophy, alarm rationalisation and the instrument list '
             'that follows from them &mdash; in that order, never the reverse.'),
            ('03', 'Build and test',
             'The panel is wired and tested in our shop, and the code is simulated '
             'against it before either one reaches your site.'),
            ('04', 'Commission and hand over',
             'Loop checks, startup, operator training, and as-built drawings that '
             'match the installation. Then annual support if you want it.'),
        ]),
        'marca3d': marca_3d(),
    }
    corpo = cabecalho(
        'Who we are', 'Controls, automation <br>and software',
        'An industrial automation integrator working out of Lakewood Ranch, Florida, '
        'with an oil and gas operation in Houston, Texas.',
        # SEM FOTOGRAFIA (19/08, a pedido): navy chapado com a reticula por
        # cima. A marca 3D ocupa a direita deste cabecalho, e fotografia +
        # reticula + peca em arame sao tres tramas no mesmo bloco -- a peca,
        # que e a mais fina das tres, e quem some.
        None, None, None,
        'Who We Are',
        # O barramento NÃO nasce mais no cabeçalho: ele começa na seção
        # "Since 2000", que já entra pela esquerda. O cabeçalho fica limpo —
        # a retícula é o desenho dele, e duas tramas no mesmo bloco brigam.
        # Por isso a marca entra por `marca=` e não por `extra=`: `extra` é o
        # trecho de barramento e liga a classe `tem-feixe`.
        marca=extras['marca3d'],
        ) + '''
<section class="secao tem-feixe">
  %(feixe_1)s
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Since 2000</p>
        <h2>Twenty-six years <br>of plants that run</h2>
      </div>
      <div class="bloco__dir">
        <p class="lead">We design, program and commission the systems that keep industrial
        processes running &mdash; and we stay reachable after startup.</p>
        <div class="pilha" style="margin-top: var(--s-5); max-width: 62ch">
          <p>i3 Automations &amp; Controls delivers advanced industrial control solutions,
          with control panels and SCADA systems at the centre of the practice. We are
          certified on the leading supervisory platforms and carry deep experience in
          wastewater treatment, paper mills and solar generation.</p>
          <p>Our work includes government contracts and solar plant projects across the
          United States. What we sell is not a product line: it is the judgement to pick a
          control strategy that fits the process, and the discipline to document it so the
          next engineer &mdash; ours or yours &mdash; can pick it up.</p>
        </div>
      </div>
    </div>
    ''' % dict(feixes, **extras) + NUMEROS + '''
  </div>
</section>

<!-- SEM BARRAMENTO AQUI, a pedido (20/08). Esta e a UNICA secao com feixe que
     tambem tem fotografia, e duas tramas no mesmo bloco brigam -- a mais fina
     e quem some. E o mesmo argumento que ja tinha tirado o barramento do
     CABECALHO desta pagina em 19/08, e ele pesa mais agora: a foto nova rende
     amplitude 30,6 contra os 15,8 da anterior, ou seja, ficou bem mais
     presente.

     O ENCADEAMENTO NAO QUEBRA, e vale entender por que. `feixe_1` sai a
     DIREITA e `feixe_3` entra pela DIREITA; o trecho que saiu daqui era
     `dir -> dir`, um corrimento reto do mesmo lado. Sem ele o barramento
     desce, passa ATRAS da secao fotografica e reaparece no mesmo x -- que e
     como um roteamento real se comporta ao passar por tras de alguma coisa,
     nao um corte. -->
<section class="secao secao--escura secao--foto"
         data-junta="inversa">
  %(foto_missao)s
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Our mission</p>
      </div>
      <div class="bloco__dir">
        <p class="citacao">Deliver automation that drives efficiency and reliability, in
        traditional and renewable energy alike.</p>
        <p class="corpo" style="margin-top: var(--s-5)">Stated plainly, because the version
        with adjectives helps nobody: high-quality automation solutions, built so our
        clients succeed in the sectors they already operate in and the ones they are
        moving into.</p>
      </div>
    </div>
  </div>
</section>

<section class="secao secao--offwhite tem-feixe"
         data-junta="inversa">
  %(feixe_3)s
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">How we work</p>
        <h2>Strategy first, <br>hardware second</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">A better transmitter will not rescue a loop that was tuned wrong,
        and a bigger PLC will not rescue logic nobody documented. We start at the process,
        then specify what it actually needs.</p>
      </div>
    </div>

    %(diagrama)s
  </div>
</section>
''' % dict(feixes, **extras) + '''
<!-- DUPLA: credenciais federais + CTA sob UMA fotografia, a pedido (20/08),
     no mesmo par que home e services ja usam.

     `--d-abre/--d-fecha` em 56-64% e nao no padrao 34-42%: a faixa livre desta
     pagina cai MAIS BAIXO que nas outras, porque o bloco de credenciais e
     longo. Abrir no padrao poria o veu aberto em cima da propria lista de
     UEI/CAGE/NAICS -- medido, o corpo caia para 1,9:1.

     `baterias` foi a UNICA do acervo a passar AA nesta caixa (1440x1560, quase
     retrato): as outras reprovam o corpo entre 3,5 e 4,1. E modulos de
     armazenamento conversam com a copy, que fala de geracao solar. -->
<div class="dupla" style="--d-abre:56%; --d-fecha:64%">
  ''' + imagem('dupla/baterias', [1280, 1920, 2560],
               'Rack of battery storage modules at an energy storage facility',
               '100vw', classe='dupla__foto') + '''
''' + GOVERNO + CONTATO_CTA + '''
</div>'''
    return pagina(
        'who-we-are.html', 'Who We Are &mdash; i3 Automations &amp; Controls',
        'Industrial automation integrator in Lakewood Ranch, Florida since 2000. '
        'Control panels, SCADA, commissioning. Certified on Ignition, VTScada and Canary.',
        # gl.js entra sozinho na frente: pagina() sabe quem consome I3GL.
        corpo, scripts_extra=('marca.js',), og_img='img/og/who-we-are-1200.jpg', trilha_seo='Who We Are')


# =========================================================== CAPABILITIES
def capacidades():
    # A foto de "Since 2000" fica sob veu BRANCO (.78 no miolo, .56 nas
    # laterais): com texto escuro sobre veu claro o pior caso e o ponto mais
    # ESCURO da foto, e ali o corpo mede 14,21:1.
    extras = {
        'foto_desde': imagem('faixa/robotica', [1280, 1920],
                             'Robotic handling cell in a distribution facility',
                             '100vw', classe='secao__foto'),
        'foto_missao': imagem('cabecalho/servicos', [1280, 1920],
                              'Relay and terminal wiring inside a control panel',
                              '100vw', classe='secao__foto'),
        'diagrama': diagrama([
            ('01', 'Understand the process',
             'P&amp;IDs, existing logic, and a conversation with whoever runs the '
             'plant at night. The constraints are rarely in the drawings.'),
            ('02', 'Choose the strategy',
             'Control philosophy, alarm rationalisation and the instrument list '
             'that follows from them &mdash; in that order, never the reverse.'),
            ('03', 'Build and test',
             'The panel is wired and tested in our shop, and the code is simulated '
             'against it before either one reaches your site.'),
            ('04', 'Commission and hand over',
             'Loop checks, startup, operator training, and as-built drawings that '
             'match the installation. Then annual support if you want it.'),
        ]),
    }
    corpo = cabecalho(
        'Capabilities', 'Eight disciplines, <br>one contractor',
        'Panel, code, network and commissioning under one roof &mdash; so nobody owns the '
        'gaps between them but us.',
        # `capacidades` e 1024x331: num cabecalho de 620 px de altura ela seria
        # AMPLIADA 1,87x e sairia borrada. `refinaria` (2560x979) e REDUZIDA
        # 0,63x na mesma caixa -- e a unica do acervo com folga aqui.
        'faixa/refinaria', [1280, 1920, 2560],
        'Refinery process units at dusk',
        'Capabilities', classe='cabecalho--foto', reticula=False) + '''
<section class="secao">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">What we deliver</p>
      </div>
      <div class="bloco__dir">
        <p class="lead">Each of these can be bought on its own. Bought together, they stop
        being four vendors pointing at each other.</p>
      </div>
    </div>
    ''' + lista_capacidades(nivel=2) + peca(
        'clp', 'data-clp',
        'PLC RACK &mdash; EXPLODED AXONOMETRIC',
        cota_peca([('06', 'modules'), ('BACKPLANE', '&rarr; TERMINALS'),
                   ('DRAG', 'to orbit')])) + '''
  </div>
</section>

<section class="secao secao--offwhite">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Platforms and certifications</p>
        <h2>Certified where <br>it matters</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Three SCADA certifications and three PLC families. The historian
        layer matters as much as the control layer: a plant that cannot prove what happened
        cannot improve, and cannot pass an audit.</p>
      </div>
    </div>
    ''' + grade_plataformas() + '''
  </div>
</section>
''' + CONTATO_CTA
    return pagina(
        'capabilities.html', 'Capabilities &mdash; i3 Automations &amp; Controls',
        'Control panels, PLC programming, SCADA, commissioning, instrumentation, '
        'industrial networks, motor controls and software development.',
        corpo, scripts_extra=('clp.js',), og_img='img/og/capabilities-1200.jpg',
        trilha_seo='Capabilities')


# ======================================================= PAST PERFORMANCE
SETORES_PP = [
    ('Automotive', 'Body shops, <br>to their standard',
     'Automotive plants do not accept a contractor&rsquo;s house style. Both of these '
     'programs were written to the customer&rsquo;s own PLC standard, which is the '
     'harder and correct way to do it.',
     [('Daimler / Mercedes-Benz',
       'Plant automation for the New Body Shop, following the Integra standard '
       'for PLC programming end to end.'),
      ('BMW',
       'F15 / F16 / F25 / F26 Body Shop SSB, integrating BMW&rsquo;s specific PLC '
       'standard programs.')],
     'setor/automotivo', [600],
     'Robotic welding line in an automotive body shop'),

    ('Oil &amp; Gas', 'Houston, and <br>150,000 tags',
     'Our oil and gas client base sits in Houston, Texas. The work is PI System '
     'expertise at scale: more than 150,000 historized tags, and the support '
     'contract that keeps them trustworthy.',
     [('Historian',
       'AVEVA PI System, 150,000+ historized tags under support.'),
      ('Scope',
       'Ongoing support and optimisation of existing control and data systems, '
       'plus new project work.')],
     'setor/oil-gas', [600, 900],
     'Process units and storage tanks at a refinery'),

    # ARCADIA ENTRA NOMEADA (21/08). O site antigo diz "a massive wastewater
    # treatment plant in Arcadia" e a migracao tinha deixado o setor sem lugar
    # nenhum. A planta e tambem a do registro de contratos logo abaixo, entao
    # nomea-la aqui e o que costura a folha de setor a tabela de cifras.
    ('Water &amp; wastewater', 'Florida plants, <br>under annual support',
     'Controls maintenance, PLC and HMI programming, and integration of the entire '
     'SCADA system. Daily reports are pulled straight from the SQL database, and '
     'every operator gets the alarm the moment something moves out of band.',
     [('Arcadia, Florida',
       'A municipal wastewater treatment plant supported for over three years: '
       'SCADA, PLC and motor control, under three successive contracts.'),
      ('Maintenance',
       'Annual support keeping control systems safe and efficient.'),
      ('Programming',
       'PLC and HMI development, with the full SCADA layer integrated rather '
       'than bolted on.'),
      ('Reporting',
       'Daily reports generated from SQL databases; alerts and alarm messages '
       'delivered to the operator on shift.')],
     'setor/agua', [600],
     'Large-diameter pipework at a water intake station'),

    # A WESTROCK VOLTOU (21/08). Ela estava nomeada no site antigo e a migracao
    # a perdeu -- e e o nome que faltava, porque ao lado de Daimler e BMW ela
    # fecha a leitura de grandes contas em TRES setores, nao em um.
    #
    # E a prosa mudou junto, por consequencia e nao por gosto: a versao anterior
    # descrevia "drives, interlocks e alarm rationalisation", que e o que um
    # controle de fabrica de papel costuma envolver -- mas NAO e o escopo que a
    # fonte registra para esta conta. Escrever o nome do cliente e manter ao
    # lado um escopo diferente do dele seria pior que nao nomear ninguem.
    # O escopo abaixo e o da fonte, palavra por palavra: painel de controle,
    # diagnostico de processo, sistemas de monitoramento e CAMERAS.
    ('Paper', 'Mill process <br>controls',
     'Paper mill process controls, where a stopped machine costs more per hour '
     'than the control system did. The work is the unglamorous kind &mdash; the '
     'panel, the fault nobody can reproduce, and the camera that finally shows '
     'what the operator has been describing for a week.',
     [('WestRock',
      'Control panel services and process troubleshooting across paper and mill '
      'operations, with monitoring systems and camera installations.'),
      ('Why it matters',
       'Continuous process: an unplanned stop is measured in tonnes, not minutes.')],
     'setor/papel', [600, 900],
     'Row of industrial presses on a mill floor'),

    ('Solar', 'Utility-scale, <br>across the country',
     'Controls and monitoring for utility-scale photovoltaic plants across the '
     'United States. Generation assets are only worth what the supervision layer '
     'can prove they produced, so the historian matters as much as the inverter.',
     [('Scope',
       'Plant controls and monitoring for utility-scale solar generation.'),
      ('Reach', 'Projects delivered across the United States.')],
     'setor/solar', [600, 900],
     'Utility-scale photovoltaic array'),

    ('Federal', 'Delivered under <br>government contract',
     'We are a registered federal contractor, and the vendor profile below is the '
     'one procurement systems ask for. The engineering does not change under a '
     'federal contract &mdash; the documentation does, and we write it either way.',
     [('UEI &middot; CAGE',
       '<span class="mono">XUZ4WKEZLS67</span> &middot; '
       '<span class="mono">9ZJM6</span>'),
      ('Primary NAICS',
       '<span class="mono">541511</span> &mdash; custom computer programming '
       'services, with six secondary codes on file.')],
     'setor/federal', [600],
     'Engineer commissioning a control system at a command station'),
]


# O resumo que fecha a pagina. Curto de proposito: o painel acima ja e o
# conteudo, e isto e a conta que o comprador leva embora.
# A fotografia de fundo entra numa FAIXA de 62%, nao na secao inteira: a fonte
# e 1920x734 e a secao tem ~630 px de altura a 1440 -- cobrir tudo obrigaria a
# ampliar, que e o erro que "Since 2000" custou. Na faixa ela e REDUZIDA 0,750x.
# A FOTO MUDOU EM 20/08, POR DOIS MOTIVOS SOMADOS.
#
#   repeticao -- `faixa/robotica` ja e a faixa full-bleed da home, e a mesma
#     foto em dois papeis foi o que a auditoria proibiu;
#   VISIBILIDADE -- o veu daqui e OFF-WHITE e cobre .78, entao so 22% da foto
#     chega a tela. O que sobrevive a isso nao e o assunto, e a AMPLITUDE.
#     Medido o p95-p5 da luminancia DEPOIS do veu: `robotica` dava 34,8, no
#     terco inferior do acervo -- por isso lia como lavagem cinza. A nova da
#     46,2.
#
# E engrenagem com corrente e um MECANISMO NEUTRO, que e o certo para "six
# sectors, one discipline": nao aponta setor nenhum, ao contrario da celula
# robotica, que apontava so o automotivo.
# Medicao completa em ferramentas/previa_ledger.py.
# A SECAO DEIXOU DE SER OFF-WHITE. Ela e agora a metade de cima de uma DUPLA,
# e a dupla e escura por construcao -- as duas secoes cedem o fundo para o
# involucro que segura a fotografia. A alternancia de superficie que esta
# secao trazia (registrada em 20/08) se perde; o que entra no lugar e o par
# lendo como um bloco unico, que foi o pedido.
# O SINOPTICO GANHOU SECAO PROPRIA (20/08). Ele estava dentro do bloco de
# abertura, espremido logo abaixo do texto de introducao: a secao e
# `--compacta` (96 px de respiro contra os 160 normais) e a peca ficava sem
# ar nenhum, encostada no paragrafo. E chegava ANTES das seis fichas, ou seja,
# antes de o visitante saber o que a pagina e.
#
# Agora ela vem DEPOIS do registro de obras, que e a ordem que a pagina conta:
# primeiro o que foi entregue, depois a tela que ficou rodando. E abre com o
# mesmo bloco de duas colunas de todas as outras secoes do site.
SINOPTICO = '''
<section class="secao secao--offwhite">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">What stays behind</p>
        <h2>The screen that <br>runs the shift</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Every one of those projects ends the same way: an operator gets a
        screen. This is what one looks like &mdash; levels, flow, pump state and the alarm
        that matters, on a plant that never stops long enough to be forgiving.</p>
      </div>
    </div>
    ''' + peca(
        'mimico', 'data-mimico',
        'SUPERVISORY MIMIC &mdash; DEMONSTRATION',
        cota_peca([('SCADA', 'screen as delivered'),
                   ('TAGS', 'generic'), ('VALUES', 'simulated')])) + '''
  </div>
</section>
'''



# ============================================ REGISTRO DE CONTRATOS
# A CAMADA QUE FALTAVA, e ela e a que o comprador federal le primeiro.
#
# O site antigo publica tres contratos com data de inicio e valor. A migracao
# tinha perdido os tres: a pagina nova contava a mesma coisa por SETOR, que le
# muito melhor para um visitante comercial e nao serve para avaliacao de past
# performance -- ali o que se pede e data, valor e referencia, e narrativa nao
# substitui nenhum dos tres.
#
# ONDE ELA ENTRA, e por que nao no fim. A ordem da pagina passa a ser:
#
#   as seis folhas de setor .... o que a empresa faz, qualitativo
#   o registro de contratos .... o que foi comprado, com data e cifra
#   o sinoptico ................ a tela que fica rodando
#   a conta final .............. 279 / 158 / 78, o agregado
#
# Especifico depois de qualitativo, agregado por ultimo. Pos-lo no fim jogaria
# o dado duro DEPOIS do numero redondo, e o numero redondo e o que menos prova.
#
# OS TRES SAO DO MESMO CLIENTE, e isso e o achado da conferencia: na fonte o
# paragrafo de Arcadia precede os tres projetos e nao ha outro cliente na
# pagina. Apresenta-los como tres clientes diferentes seria inventar alcance;
# apresenta-los como um programa de tres contratos e o que a fonte diz -- e le
# melhor, porque relacao que se renova tres vezes em tres anos prova mais que
# tres trabalhos avulsos.
#
# ORDEM CRONOLOGICA, nao a da fonte. La eles saem 09/2022, 03/2024, 08/2021 --
# sem ordem nenhuma. Em ordem, a tabela conta que a relacao comecou em 2021 e
# ainda estava sendo renovada em 2024, que e exatamente a leitura que "over
# three years" afirma em prosa.
CONTRATOS_PP = '''
<section class="secao secao--offwhite">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Contract record</p>
        <h2>Three contracts, <br>one plant</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">The sheets above are what we do. This is what was bought. A
        municipal wastewater treatment plant in Arcadia, Florida has renewed with us
        three times since 2021 &mdash; SCADA, PLC and motor control on a facility that
        cannot be taken offline to be fixed.</p>
      </div>
    </div>
    ''' + contratos(
        'SCADA support &mdash; wastewater treatment plant, Arcadia, Florida',
        [('08 / 16 / 2021', '&mdash;', '$150,000.00'),
         ('09 / 21 / 2022', '&mdash;', '$35,000.00'),
         ('03 / 18 / 2024', '04 / 30 / 2024', '$99,450.00')],
        ('Three contracts, combined', '$284,450.00'),
        # A nota absorveu a coluna "Reference", que trazia o MESMO texto nas
        # tres linhas. Ela diz o que a coluna dizia, uma vez so, e no lugar
        # onde uma nota de rodape pertence.
        '<b>References for all three are provided on request</b>, with the '
        'plant&rsquo;s consent. Where no end date is shown, none is recorded '
        'against that contract.') + '''
  </div>
</section>
'''

RESUMO_PP = '''
<section class="secao secao--escura"
         data-junta="inversa">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">The ledger</p>
        <h2>Twenty-six years, <br>counted</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Six sectors, one discipline. What changes between a refinery and
        a body shop is the process and the consequence of getting it wrong &mdash; not the
        rigor the control system deserves. The numbers below are projects delivered, not
        proposals written.</p>
      </div>
    </div>
    ''' + NUMEROS + '''
  </div>
</section>
'''


def desempenho():
    """Past performance: a pagina que o cliente marcou como o diferencial.

    Era uma pilha de quatro secoes iguais -- bloco de texto mais tabela de
    dados, repetido. Cada setor tinha o mesmo peso visual e o mesmo layout,
    entao a pagina lia como relatorio: nada dizia onde olhar, e um comprador
    que entrasse procurando o SEU setor tinha de varrer tudo.

    Agora e um painel PRESO: um setor por vez, a rolagem avanca, as setas
    giram e a volta e infinita. Cada setor ocupa a tela quando e a vez dele,
    com a fotografia montada ao lado da tese e dos dados.
    """
    # O bloco que apresenta o registro. Ele existe porque a pagina nao pode
    # saltar do cabecalho direto para a primeira ficha: sem uma frase que diga
    # o que a pilha e, as seis fichas comecam do nada -- que era metade da
    # queixa de "as secoes nao se conectam suavemente". As outras oito paginas
    # do site abrem toda secao com este mesmo bloco de duas colunas; esta era a
    # unica que nao abria.
    abertura = '''
<section class="secao secao--compacta">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">The record</p>
        <h2>Six sectors, <br>one discipline</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Each sheet below is one sector: what the plant had to do, who it
        was for, and what we were responsible for. What changes between a refinery and a
        body shop is the process and the consequence of getting it wrong &mdash; not the
        rigor the control system deserves.</p>
      </div>
    </div>
  </div>
</section>'''

    corpo = cabecalho(
        'Past performance', 'What already <br>runs in the field',
        '279 automation projects worldwide, 158 in the United States, 78 in Florida. '
        'These are some of them.',
        'cabecalho/projetos', [1125],
        'Robotic cell assembling a vehicle body',
        'Past Performance', reticula=False) + abertura + registro_obras(SETORES_PP) + CONTRATOS_PP + SINOPTICO         + '''
<!-- DUPLA: o resumo e o CTA sob UMA fotografia. `--d-abre/--d-fecha` em
     42-52%: a faixa livre daqui fica entre o fim da banda de numeros e o
     eyebrow do CTA. -->
<div class="dupla" style="--d-abre:42%; --d-fecha:52%">
  ''' + imagem('dupla/engrenagem', [1280, 1920, 2560],
               'Gear and roller chain drive on industrial machinery',
               '100vw', classe='dupla__foto') + '''
''' + RESUMO_PP + CONTATO_CTA + '''
</div>'''
    return pagina(
        'past-performance.html', 'Past Performance &mdash; i3 Automations &amp; Controls',
        'Daimler/Mercedes-Benz New Body Shop, BMW F15/F16/F25/F26 SSB, PI System with '
        '150,000+ tags in Houston, Florida water utilities and U.S. solar.',
        # `setores.js` SAIU junto com o carrossel: o registro nao tem estado, e
        # a unica coisa que se move nele e `reveal`, que o main.js ja resolve.
        corpo, scripts_extra=('mimico.js',), og_img='img/og/past-performance-1200.jpg', trilha_seo='Past Performance')


# =============================================================== SERVICES
def servicos():
    """Mode PERSUADE: o visitante decide e age.

    A pagina apresenta o PRODUTO, em quatro perguntas na ordem em que um
    comprador as faz: como eu contrato, o que vem na caixa, como o trabalho
    corre, e em que voces trabalham. Cada uma tem um componente proprio, e
    nenhum deles e um card generico.
    """
    corpo = cabecalho(
        'Services', 'How you buy <br>the work',
        'Project, retrofit or annual support &mdash; and the option to design your own '
        'system with us instead of taking ours off the shelf.',
        'cabecalho/servicos', [1280, 1920],
        'Relay and terminal wiring inside a control panel',
        'Services', reticula=False) + '''
<section class="secao" id="engagements">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Engagements</p>
        <h2>Three ways <br>this usually starts</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Most of our work arrives as one of these three. Any of them can
        turn into the others, and often does &mdash; a support contract that uncovers an
        obsolete PLC becomes a retrofit, and a retrofit that goes well becomes the next
        new system.</p>
      </div>
    </div>
    ''' + oferta(
        [('New system', 'Greenfield or full replacement'),
         ('Retrofit &amp; migration', 'Current plant, obsolete controls'),
         ('Annual support', 'Systems already running')],
        [('Starts when',
          ['You have a process and no control system, or one at the end of its life.',
           'The plant runs, but the PLC, HMI or historian is obsolete or '
           'unsupported.',
           'A system is live and has to stay live &mdash; ours or someone '
           'else&rsquo;s.']),
         ('What we do',
          ['Control philosophy, panel design and build, PLC and SCADA development, '
           'instrumentation, commissioning and handover.',
           'Assessment, migration plan, and a cutover that fits inside the outage '
           'window you actually have.',
           'Scheduled checks, remote diagnosis, corrective work, and the reporting '
           'that proves the plant behaved.']),
         ('Typical trigger',
          ['A new line, a new plant, or a permit that requires monitoring you '
           'cannot produce today.',
           'No spares left, a vendor that dropped support, or a historian nobody '
           'can query any more.',
           'Staff turnover, an expiring warranty, or alarms the operators have '
           'stopped trusting.']),
         ('You end up with',
          ['A documented system and drawings that match what is on the wall.',
           'Current hardware on the same process, without the operators having to '
           'relearn their plant.',
           'An engineer who already knows your process before you call.'])]) + '''
  </div>
</section>

<section class="secao secao--offwhite" id="deliverables">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">In every scope</p>
        <h2>What leaves <br>with you</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">The same four things ship with every engagement above, and they
        are yours. An integrator who keeps the source code is selling you a dependency,
        not a control system.</p>
      </div>
    </div>

    <div class="dados reveal" style="margin-top: var(--gap-bloco)">
      <div class="dados__linha"><p class="dados__rotulo">Drawings</p>
      <p class="dados__valor">Panel schematics, loop sheets and as-builts that match what
      is installed &mdash; not what was designed six months earlier.</p></div>
      <div class="dados__linha"><p class="dados__rotulo">Code</p>
      <p class="dados__valor">Commented PLC and HMI source, delivered to you, in the
      platform&rsquo;s native format. No locked blocks, no runtime we hold the key to.</p></div>
      <div class="dados__linha"><p class="dados__rotulo">Test records</p>
      <p class="dados__valor">Factory acceptance results from our shop, and site
      loop-check records signed off during commissioning.</p></div>
      <div class="dados__linha"><p class="dados__rotulo">Training</p>
      <p class="dados__valor">Operator and maintenance handover at your console, on your
      process, with the people who will run it at 3 a.m.</p></div>
    </div>
  </div>
</section>

<section class="secao" id="method">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">How the work runs</p>
        <h2>Strategy first, <br>hardware second</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">The same four steps on every engagement. The numbers here are a
        real sequence &mdash; each step is the input to the next, and skipping one is how
        a project ends up with a bigger PLC and the same bad loop.</p>
      </div>
    </div>
    ''' + diagrama([
        ('01', 'Understand the process',
         'P&amp;IDs, existing logic, and a conversation with whoever runs the '
         'plant at night. The constraints are rarely in the drawings.'),
        ('02', 'Choose the strategy',
         'Control philosophy, alarm rationalisation and the instrument list '
         'that follows from them &mdash; in that order, never the reverse.'),
        ('03', 'Build and test',
         'The panel is wired and tested in our shop, and the code is simulated '
         'against it before either one reaches your site.'),
        ('04', 'Commission and hand over',
         'Loop checks, startup, operator training, and as-built drawings that '
         'match the installation. Then annual support if you want it.'),
    ]) + '''
  </div>
</section>

<section class="secao secao--offwhite" id="platforms">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Platforms</p>
        <h2>What we are <br>certified to run</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">A filled contact is a platform we are certified on; an open one
        is a platform we work in. Which one your project uses is a decision about the
        process and about who maintains it after we leave.</p>
      </div>
    </div>
    ''' + grade_plataformas() + '''
  </div>
</section>

''' + '''
<!-- AS DUAS SECOES QUE FECHAM SERVICES DIVIDEM UMA FOTOGRAFIA SO. Antes eram
     duas fotos diferentes (refinaria em cima, teclado embaixo) e a emenda
     saltava no meio de um bloco que se le como um so.

     `dupla/comando` -- mesa de comando, mao no joystick -- e nao um painel:
     o cabecalho desta pagina ja e um close de reles e bornes, e duas fotos de
     painel na mesma pagina leem como a mesma foto duas vezes. A fonte tem
     6000 px de largura, entao a maior saida (2560) ja e uma REDUCAO de 0,43x,
     e na caixa de 1440 ela cai para 0,69x. -->
<div class="dupla">
  ''' + imagem('dupla/comando', [1280, 1920, 2560],
               'Operator hand on a joystick at a control desk with pushbuttons '
               'and HMI screens',
               '100vw', classe='dupla__foto') + '''
<section class="secao secao--escura" id="reporting">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Your design or ours</p>
        <h2>Total control <br>and monitoring</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">You can take one of our proven designs, or build a new one with
        us. Either way the outcome is the same: daily reporting that runs itself, and
        every operator getting the alert and the alarm message the moment an issue
        appears.</p>
        ''' + cta('contact.html', 'Send us the scope') + '''
      </div>
    </div>
    ''' + peca(
        'malha', 'data-malha',
        'PID CONTROL LOOP &mdash; DRAG THE SETPOINT',
        cota_peca([('PLANT', 'first order + dead time'),
                   ('LOOP', 'PID, tuned to the process'),
                   ('DRAG', 'the setpoint')])) + '''
  </div>
</section>
''' + CONTATO_CTA + '''
</div>'''
    return pagina(
        'services.html', 'Services &mdash; i3 Automations &amp; Controls',
        'New control systems, retrofit and migration, and annual controls support. '
        'Drawings, commented code, test records and operator training in every scope.',
        corpo, scripts_extra=('malha.js',), og_img='img/og/services-1200.jpg',
        trilha_seo='Services')


# ================================================================ GALLERY
GALERIA = [
    # Legenda descreve a CENA, `alt` descreve para quem nao ve. Os dois foram
    # escritos olhando cada arquivo -- alt escrito longe da imagem envelhece
    # errado, e este projeto ja corrigiu dois por isso.
    #
    # A ORDEM E CURADORIA, E ELA TEM UMA CONSEQUENCIA VISUAL. As 9 fotografias
    # autorais do cliente sao todas 600x600, e elas lideram o acervo -- e a
    # escolha editorial certa, sao o material mais valioso da pagina. Mas
    # enfileiradas em bloco elas dao ao empilhamento nove pecas de altura
    # IDENTICA, e as duas primeiras fileiras do mosaico voltavam a ser uma
    # grade -- exatamente o defeito que a proporcao nativa veio corrigir.
    #
    # Por isso `clarificador` (0,80, retrato) e `celula` (1,50, paisagem) foram
    # trazidas para as posicoes 3 e 6: a terceira coluna se desloca ja na
    # primeira fileira e o mosaico le como mosaico desde o topo. As duas sao
    # aberturas fortes por conta propria -- bacias de decantacao e celula
    # robotizada --, entao a curadoria nao perde nada com a troca.
    ('galeria/painel', [600], 'Technician working inside a live control panel',
     'Panel maintenance in the field'),
    ('galeria/scada', [600],
     'SCADA screen showing effluent station discharge flow, with a hard hat in '
     'the foreground', 'Effluent discharge flow, on shift'),
    ('galeria/clarificador', [400, 800],
     'Rectangular clarifier basins with walkways at a wastewater treatment plant',
     'Clarifier basins, wastewater treatment'),
    ('galeria/painel-campo', [600],
     'Field-installed control panel with pilot lights and selector switches, '
     'door open', 'Pump station panel, open for commissioning'),
    ('galeria/bomba', [600],
     'Submersible pump set being lowered by crane into a wet well',
     'Submersible set going into the wet well'),
    ('galeria/celula', [400, 800], 'Robotic cell assembling a vehicle body',
     'Robotic assembly cell'),
    ('galeria/obra-agua', [600],
     'Controls cabinet being installed beside weir gates under construction',
     'Weir gate structure, controls going in'),
    ('galeria/captacao', [600], 'Large-diameter pipework at a raw water intake',
     'Raw water intake, Florida'),
    ('galeria/body-in-white', [600],
     'Robots welding a car body on an automotive line',
     'Automotive body shop, body-in-white'),
    # 1,59 entre dois 1,00: quebra a corrida de quadrados das autorais, e
    # fica junto do bloco automotivo, que e onde ela pertence.
    ('galeria/robo-linha', [400, 800],
     'Six-axis robot arm serving an automated assembly line inside a '
     'production hall',
     'Robot on the assembly line'),
    ('galeria/bancada', [600], 'Engineer programming at a control panel workbench',
     'Panel programming and bench testing'),
    # Mesma fonte de `dupla/clp`, aqui na proporcao nativa. Fecha o grupo de
    # painel -- manutencao, programacao, interior e fiacao em sequencia.
    ('galeria/painel-clp', [400, 800],
     'Open control panel with PLC racks, circuit breakers, terminal blocks and '
     'wiring ducts',
     'Control panel interior, PLC racks'),
    ('galeria/fiacao', [422],
     'Hands wiring contactors and circuit breakers inside a control panel',
     'Panel wiring, contactors and breakers'),
    ('galeria/comissionamento', [600],
     'Engineer commissioning a system from a laptop at a command station',
     'Commissioning from the command station'),
    # Mesma fonte de `dupla/comando`. Entra ANTES de `sala-controle` (0,80)
    # de proposito: 1,00 / 1,50 / 0,80 / 1,50 alterna, enquanto depois dela
    # cairia num corredor de quatro 1,50 seguidos.
    ('galeria/mesa-comando', [400, 800],
     'Operator hand on a joystick at a control desk with illuminated '
     'pushbuttons and HMI screens',
     'Control desk, operator station'),
    ('galeria/sala-controle', [400, 800],
     'Operator in a high-visibility vest at a control room console with SCADA screens',
     'Control room, live process'),
    ('galeria/campo', [400, 800],
     'Two technicians in coveralls at a robot teach pendant on a plant floor',
     'Field review at the teach pendant'),
    ('galeria/braco-bancada', [400, 800],
     'Orange six-axis industrial robot arm mounted on a workbench',
     'Six-axis arm, bench setup'),
    ('galeria/bornes', [400, 800],
     'Relay modules wired to a terminal block inside a control panel',
     'Relays and terminal block'),
    ('galeria/teclado', [400, 800],
     'Hand pressing an illuminated membrane keypad on a machine control panel',
     'Membrane keypad, machine control'),
    ('galeria/refinaria', [400, 800],
     'Process units and storage tanks at a refinery',
     'Refinery process units'),
    ('galeria/prensas', [400, 800],
     'Row of industrial stamping presses on a mill floor',
     'Press line, mill floor'),
    ('galeria/prensa-detalhe', [400, 800],
     'Close view of the tooling under an industrial press',
     'Press tooling, close'),
    # 1,33 no meio da corrida mais longa de 1,50 do acervo (posicoes 17 a 23):
    # e o unico lugar em que ela paga aluguel na composicao.
    ('galeria/solda-placa', [400, 800],
     'Soldering iron working on a control board with switches and indicator '
     'LEDs',
     'Control board assembly, bench detail'),
    ('galeria/engrenagens', [400, 800],
     'Meshed gears and chain drive on industrial machinery',
     'Gear and chain drive'),
    ('galeria/agv', [400, 800],
     'Automated guided vehicle handling totes in warehouse racking',
     'Automated handling in racking'),
    ('galeria/britagem', [400, 800],
     'Conveyor and stockpile at an aggregate processing plant',
     'Conveyor and stockpile'),
    ('galeria/fiacao-textil', [400, 800],
     'Continuous filament running through a fibre processing machine',
     'Continuous filament, process line'),
    ('galeria/baterias', [400, 800],
     'Racked battery modules in an energy storage installation',
     'Battery modules, energy storage'),
    ('galeria/solar-campo', [400, 800],
     'Aerial view of a ground-mounted solar farm beside farmland',
     'Ground-mounted solar, from the air'),
    ('galeria/solar-aereo', [400, 800],
     'Rows of photovoltaic panels on a utility-scale solar plant',
     'Utility-scale photovoltaic rows'),
    ('galeria/solar-painel', [400, 800],
     'Close view of photovoltaic modules on a mounting structure',
     'Module and mounting structure'),
    ('galeria/linha-solar', [400, 800],
     'Worker in a hard hat looking down a photovoltaic module production line',
     'Module production line'),
]


def _proporcao(base, larguras):
    """Proporcao real dos arquivos que ESTA PAGINA vai referenciar.

    Ela vai para o HTML como `--ar` e vira `aspect-ratio` na moldura, o que faz
    a coluna ter a altura CERTA antes de a fotografia chegar. Sem isso o
    mosaico monta com 29 caixas de altura zero e desaba para a altura final
    conforme cada imagem baixa -- e num acervo de 29 fotos esse rearranjo e
    justamente a sensacao de "as fotos demoram e a pagina pula".

    MEDE AS LARGURAS DECLARADAS, uma a uma, e EXIGE que concordem. Nao e
    paranoia: a primeira versao varria a pasta e devolvia a primeira largura
    que achasse, e isso escondeu um defeito real. Quando `build_imagens`
    passou a preservar a proporcao nativa, quatro fotos mudaram de faixa de
    largura (de 750 para 400/800) -- e os arquivos de 750, gerados no recorte
    QUADRADO antigo, continuaram no disco. A varredura de referencias passava
    (o arquivo existia), a pagina referenciava o quadrado velho, e `--ar`
    vinha medido dele: 1.0. Tudo consistente, tudo errado.

    Medindo o que a pagina realmente pede, o mesmo erro vira uma quebra de
    build com o nome do arquivo. Um arquivo que sobra e mais perigoso que um
    que falta, porque nada acusa.
    """
    from PIL import Image
    caminho = os.path.join(os.path.dirname(__file__), '..', 'site', 'img',
                           base.replace('/', os.sep))

    def medir(w, exts):
        for suf in exts:
            f = '%s-%d.%s' % (caminho, w, suf)
            if os.path.exists(f):
                with Image.open(f) as im:
                    return im.width / im.height
        raise SystemExit('%s-%d.{%s} nao existe: rode build_imagens.py'
                         % (base, w, ','.join(exts)))

    # A maior largura e a unica que tem o formato BASE (`salvar()` so emite jpg
    # ali; as menores saem em avif/webp, que sao o que o srcset consome). Ela e
    # tambem a que o `<img src>` aponta, entao e a medida certa.
    r = medir(larguras[-1], ('jpg', 'png'))
    # As menores existem? A proporcao delas e a mesma por construcao -- `salvar`
    # redimensiona proporcionalmente --, entao o que se confere aqui e
    # PRESENCA, nao forma. Sem esta linha, uma largura declarada e nunca
    # gerada vira um `srcset` apontando para o vazio, e o navegador cai no
    # `src` sem reclamar de nada.
    for w in larguras[:-1]:
        medir(w, ('webp',))
    return r


def _empilhar(itens, colunas):
    """Distribui as figuras em N colunas, sempre na MAIS CURTA ate agora.

    Round-robin (`i % n`) seria uma linha e esta errado: com proporcoes de 0,66
    a 1,60 as tres colunas terminariam com centenas de pixels de diferenca. O
    guloso pela coluna mais curta e o mesmo criterio que `columns` do CSS usa
    internamente -- a diferenca e que aqui as colunas sao elementos de verdade,
    e por isso cada uma pode ter a propria deriva de rolagem.

    A altura de cada peca em unidades de LARGURA DE COLUNA e `1 / proporcao`
    mais a legenda; e o suficiente para equilibrar, e nao depende de a imagem
    ja ter carregado.
    """
    LEGENDA = .18                      # legenda + goteira, em larguras de coluna
    pilhas = [[] for _ in range(colunas)]
    alturas = [0.0] * colunas
    for item in itens:
        k = alturas.index(min(alturas))
        pilhas[k].append(item)
        alturas[k] += 1 / item[4] + LEGENDA
    return pilhas


def galeria():
    """Mode EXPERIENCE: a fotografia lidera, a interface recua.

    O QUE FALTAVA AQUI ERA VARIACAO, NAO ANIMACAO. O pedido foi "uma biblioteca
    de imagens precisa de mais movimento", e a primeira medicao explicou por
    que a pagina parecia parada: `build_imagens.galeria()` recortava TODAS as
    29 fotos em 1:1, entao o "mosaico por colunas" era, na pratica, uma grade
    de 29 quadrados iguais. Nenhuma quantidade de animacao conserta isso -- uma
    grade uniforme continua uniforme se mexer.

    Corrigido na origem: a galeria passou a sair na proporcao NATIVA de cada
    fonte, aparada em 0,66..1,60. Agora ha retrato, quadrado e paisagem na
    mesma coluna, e o mosaico e um mosaico.

    COLUNAS DE VERDADE, NAO `columns`. A propriedade `columns` do CSS montava
    isto sozinha, e foi trocada por tres elementos por um motivo so: coluna que
    e elemento pode ter DERIVA PROPRIA na rolagem. E o que da profundidade a um
    acervo -- as colunas correm em velocidades ligeiramente diferentes, e o
    plano se abre. Com `columns` nao ha o que animar: e uma caixa so.

    E A DERIVA NAO E DESLOCAMENTO PARADO. As tres colunas nascem ALINHADAS no
    topo e so se separam enquanto a pagina rola. Escalonar a origem delas seria
    repetir a "escada que sobe e desce" que o usuario acabou de reprovar na
    prancha da home -- e ele tem razao: o site alinha, e o movimento e que
    quebra o alinhamento, nunca o repouso.
    """
    itens = [(base, larg, alt, leg, _proporcao(base, larg))
             for base, larg, alt, leg in GALERIA]

    def figura(item, n):
        base, larg, alt, leg, ar = item
        return (
            '<figure class="galeria__figura" data-progresso data-ar="%.4f" '
            'data-ordem="%d" style="--ar:%.4f">'
            '<div class="galeria__item">%s'
            '<span class="galeria__marca" aria-hidden="true"></span>'
            '</div>'
            '<figcaption class="galeria__legenda">'
            '<span class="galeria__num">%02d</span>'
            '<span class="galeria__txt">%s</span>'
            '</figcaption></figure>'
            % (ar, n - 1, ar,
               imagem(base, larg, alt,
                      '(max-width: 700px) 92vw, (max-width: 1100px) 46vw, 30vw'),
               n, leg))

    ordem = {id(it): i for i, it in enumerate(itens)}
    colunas = ''.join(
        '<div class="galeria__coluna" style="--c:%d">%s</div>'
        % (c, ''.join(figura(it, ordem[id(it)] + 1) for it in pilha))
        for c, pilha in enumerate(_empilhar(itens, 3)))

    corpo = cabecalho(
        'Gallery', 'The work, <br>and where it happens',
        'Panels, control rooms, plant floors and the plants themselves &mdash; '
        'the environments this company builds control systems for.',
        'cabecalho/galeria', [1125],
        'Industrial robot arm in a production cell',
        'Gallery', reticula=False) + '''
<section class="secao">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">The archive</p>
      </div>
      <div class="bloco__dir">
        <!-- A afirmacao "every photograph here is from a job we did" SAIU, e a
             saida foi deliberada: a galeria mostra o acervo inteiro, e nem toda
             foto e de obra propria. Uma pagina que AFIRMA autoria e mostra
             outra coisa e pior do que uma que nao afirma nada. -->
        <p class="lead">Some of these are our own jobs, photographed on site. Others are
        the kind of plant and equipment we work in every week. Together they are the
        environment the control systems on this site live in.</p>
        <p class="galeria__conta mono">%d plates &middot; panels, commissioning, control
        rooms, water, automotive and solar</p>
      </div>
    </div>
  </div>
  <div class="galeria__mosaico" data-mosaico data-progresso data-colunas="3">%s</div>
</section>
''' % (len(itens), colunas) + CONTATO_CTA
    return pagina(
        'gallery.html', 'Gallery &mdash; i3 Automations &amp; Controls',
        'Photographs from i3Automations projects and the industrial environments we '
        'work in: control panels, commissioning, control rooms, water plants and solar.',
        # `mosaico.js` so REEMPILHA quando o numero de colunas muda. O
        # empilhamento inicial vem pronto do gerador, entao a pagina sem
        # JavaScript continua com as tres colunas equilibradas.
        corpo, scripts_extra=('mosaico.js',), og_img='img/og/gallery-1200.jpg', trilha_seo='Gallery')


# ================================================================ CONTACT
def contato():
    redes = ''.join(
        '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>'
        % (u, n) for n, u in REDES)

    # A foto de "Since 2000" fica sob veu BRANCO (.78 no miolo, .56 nas
    # laterais): com texto escuro sobre veu claro o pior caso e o ponto mais
    # ESCURO da foto, e ali o corpo mede 14,21:1.
    extras = {
        'foto_desde': imagem('faixa/robotica', [1280, 1920],
                             'Robotic handling cell in a distribution facility',
                             '100vw', classe='secao__foto'),
        'foto_missao': imagem('cabecalho/servicos', [1280, 1920],
                              'Relay and terminal wiring inside a control panel',
                              '100vw', classe='secao__foto'),
        'diagrama': diagrama([
            ('01', 'Understand the process',
             'P&amp;IDs, existing logic, and a conversation with whoever runs the '
             'plant at night. The constraints are rarely in the drawings.'),
            ('02', 'Choose the strategy',
             'Control philosophy, alarm rationalisation and the instrument list '
             'that follows from them &mdash; in that order, never the reverse.'),
            ('03', 'Build and test',
             'The panel is wired and tested in our shop, and the code is simulated '
             'against it before either one reaches your site.'),
            ('04', 'Commission and hand over',
             'Loop checks, startup, operator training, and as-built drawings that '
             'match the installation. Then annual support if you want it.'),
        ]),
    }
    corpo = cabecalho(
        'Contact', 'Tell us what the <br>process has to do',
        'Two phone lines, one inbox, and an engineer on the other end of all three.',
        'cabecalho/contato', [1280, 1920],
        'Hand pressing an illuminated membrane keypad on a machine control panel',
        'Contact', reticula=False) + '''
<section class="secao">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Reach us directly</p>
      </div>
      <div class="bloco__dir">
        <p class="lead">There is no contact form on this page on purpose. A form adds a
        step and answers nothing; a phone number and an inbox reach the same people
        faster.</p>
        <p class="corpo" style="margin-top: var(--s-4)">Send the scope, the P&amp;ID, or
        just the problem. If the answer is that you do not need us, we will say that
        too.</p>
      </div>
    </div>

    <div class="contato reveal">
      <div class="contato__bloco">
        <p class="contato__rotulo">Sales &amp; Services</p>
        <p class="contato__valor"><a href="tel:+14078200299">%(vendas)s</a></p>
        <p class="contato__nota">New projects, quotes and scoping. Also on
        <a class="link" href="%(zap)s" target="_blank" rel="noopener">WhatsApp</a>.</p>
      </div>
      <div class="contato__bloco">
        <p class="contato__rotulo">Support</p>
        <p class="contato__valor"><a href="tel:+19416661880">%(suporte)s</a></p>
        <p class="contato__nota">Systems already running, and annual support
        contracts.</p>
      </div>
      <div class="contato__bloco">
        <p class="contato__rotulo">E-mail</p>
        <p class="contato__valor"><a href="mailto:%(email)s">%(email)s</a></p>
        <p class="contato__nota">Best channel for drawings, scope documents and RFQs.</p>
      </div>
      <div class="contato__bloco">
        <p class="contato__rotulo">Offices</p>
        <p class="contato__valor">Lakewood Ranch, FL</p>
        <p class="contato__nota">Oil &amp; Gas operation in Houston, TX.</p>
      </div>
    </div>
  </div>
</section>

<section class="secao secao--offwhite">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">For contracting officers</p>
        <h2>Everything you <br>need to register us</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Our vendor profile in the format procurement systems ask for. If
        something else is required for your solicitation, ask on either line and we will
        send it the same day.</p>
      </div>
    </div>

    <div class="credencial reveal">
      <div class="credencial__item"><p class="credencial__rotulo">Legal name</p>
      <p class="contato__valor" style="margin-top: var(--s-2)">i3 Automations &amp;
      Controls</p></div>
      <div class="credencial__item"><p class="credencial__rotulo">UEI</p>
      <p class="credencial__valor">XUZ4WKEZLS67</p></div>
      <div class="credencial__item"><p class="credencial__rotulo">CAGE</p>
      <p class="credencial__valor">9ZJM6</p></div>
      <div class="credencial__item"><p class="credencial__rotulo">Primary NAICS</p>
      <p class="credencial__valor">541511</p></div>
      <div class="credencial__item"><p class="credencial__rotulo">Secondary NAICS</p>
      <p class="credencial__valor credencial__valor--multi">238210 &middot; 334513 &middot;
      335313 &middot; 518210 &middot; 541330 &middot; 541512</p></div>
      <div class="credencial__item"><p class="credencial__rotulo">Certifications</p>
      <p class="contato__valor" style="margin-top: var(--s-2)">Ignition &middot; VTScada
      &middot; Canary</p></div>
    </div>
  </div>
</section>

<!-- A secao usava `.rodape__lista` -- um componente do RODAPE -- com tres
     `style` inline reescrevendo a grade dele por cima. Componente emprestado
     de outro contexto mais remendo inline e como um layout deixa de ter dono:
     mexer no rodape quebrava esta pagina, e nada dizia isso.
     `.canais` e o componente proprio, e o bloco passou a ter titulo: "Elsewhere"
     sozinho num eyebrow nao dizia o que a lista e. -->
<section class="secao secao--escura secao--compacta">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">Elsewhere</p>
        <h2>Where else <br>we show up</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">Project photographs, commissioning notes and the occasional
        panel build. The phone and the e-mail above are still the fastest way to reach
        someone.</p>
        <ul class="canais" role="list">%(redes)s</ul>
      </div>
    </div>
    %(carta)s
  </div>
</section>
''' % {'vendas': TEL_VENDAS, 'suporte': TEL_SUPORTE, 'email': EMAIL,
       'zap': WHATSAPP, 'redes': redes,
       # A peca entra pelo DICIONARIO e nao partindo a string. Partir troca
       # `'''A''' % d` por `'''A''' + x + '''B''' % d`, e em Python o `%` liga
       # mais forte que o `+`: so o ULTIMO fragmento recebe o dicionario, e
       # todos os `%(chave)s` anteriores ficam literais no HTML. Foi o que
       # aconteceu -- a varredura acusou `%(zap)s` como referencia quebrada.
       'carta': peca(
           'carta', 'data-carta',
           'LAKEWOOD RANCH, FL &mdash; HOUSTON, TX',
           cota_peca([('2', 'operations'), ('MERCATOR', 'WGS 84'),
                      ('GREAT CIRCLE', 'plotted')]))}
    return pagina(
        'contact.html', 'Contact &mdash; i3 Automations &amp; Controls',
        'Sales and Services +1 (407) 820-0299, Support +1 (941) 666-1880, '
        'acastro@i3automations.com. Lakewood Ranch, Florida and Houston, Texas.',
        corpo, scripts_extra=('carta.js',), og_img='img/og/contact-1200.jpg',
        trilha_seo='Contact')


# ================================================================= LEGAIS
def legal(arquivo, titulo, eyebrow, h1, lead, secoes, img, larg, alt, trilha):
    blocos = ''.join('<h2>%s</h2>%s' % (t, c) for t, c in secoes)
    # A foto de "Since 2000" fica sob veu BRANCO (.78 no miolo, .56 nas
    # laterais): com texto escuro sobre veu claro o pior caso e o ponto mais
    # ESCURO da foto, e ali o corpo mede 14,21:1.
    extras = {
        'foto_desde': imagem('faixa/robotica', [1280, 1920],
                             'Robotic handling cell in a distribution facility',
                             '100vw', classe='secao__foto'),
        'foto_missao': imagem('cabecalho/servicos', [1280, 1920],
                              'Relay and terminal wiring inside a control panel',
                              '100vw', classe='secao__foto'),
        'diagrama': diagrama([
            ('01', 'Understand the process',
             'P&amp;IDs, existing logic, and a conversation with whoever runs the '
             'plant at night. The constraints are rarely in the drawings.'),
            ('02', 'Choose the strategy',
             'Control philosophy, alarm rationalisation and the instrument list '
             'that follows from them &mdash; in that order, never the reverse.'),
            ('03', 'Build and test',
             'The panel is wired and tested in our shop, and the code is simulated '
             'against it before either one reaches your site.'),
            ('04', 'Commission and hand over',
             'Loop checks, startup, operator training, and as-built drawings that '
             'match the installation. Then annual support if you want it.'),
        ]),
    }
    corpo = cabecalho(eyebrow, h1, lead, img, larg, alt, trilha) + '''
<section class="secao">
  <div class="container">
    <div class="texto-legal reveal">%s</div>
  </div>
</section>''' % blocos
    # O nome da migalha sai do proprio titulo, ate o travessao -- assim ele
    # nao vira uma terceira copia de um texto que ja existe duas vezes.
    return pagina(arquivo, titulo, lead.replace('<br>', ' '), corpo,
                  trilha_seo=titulo.split('&mdash;')[0].strip())


PRIVACIDADE = [
    ('Who this policy covers',
     '<p>This policy applies to i3 Automations &amp; Controls (&ldquo;i3Automations&rdquo;, '
     '&ldquo;we&rdquo;, &ldquo;us&rdquo;) and to this website. It explains what we collect '
     'when you visit or contact us, and what we do with it.</p>'),
    ('What we collect',
     '<p>This site has no contact form, no analytics tags, no advertising pixels and no '
     'third-party scripts. Every asset &mdash; fonts included &mdash; is served from our '
     'own domain, so browsing these pages does not report your visit to anyone else.</p>'
     '<ul><li><strong>Nothing automatic beyond server logs.</strong> Our host records '
     'standard request data such as IP address, timestamp and requested URL, kept only for '
     'security and reliability.</li>'
     '<li><strong>What you send us.</strong> If you e-mail, call or message us on WhatsApp, '
     'we hold what you send: your name, contact details and the content of your '
     'enquiry.</li>'
     '<li><strong>One local preference.</strong> Your light or dark theme choice is stored '
     "in your browser's local storage. It never leaves your device and we cannot read "
     'it.</li></ul>'),
    # A SECAO NOVA EXISTE PORQUE A FAIXA APONTA PARA CA. Uma faixa de
    # consentimento que leva a uma pagina sem nada sobre armazenamento deixa o
    # visitante sem como conferir o que ela afirmou -- e o que ela afirma aqui
    # e incomum (nenhum cookie), entao e justamente o que precisa de prova.
    # O texto NAO promete "we use cookies to improve your experience": este
    # site nao poe cookie nenhum, e escreve-lo criaria a contradicao que a
    # secao existe para fechar.
    ('Cookies and local storage',
     '<p><strong>This site sets no cookies.</strong> Not for analytics, not for '
     'advertising, not for sessions. Nothing this site stores is ever attached to a '
     'request, so nothing about your browsing reaches us or anyone else.</p>'
     '<p>Two values are kept in your browser&rsquo;s local storage, which is a store '
     'that stays on your device and is never transmitted:</p>'
     '<ul><li><strong>Your theme choice</strong> &mdash; light or dark, so the site '
     'opens the way you left it.</li>'
     '<li><strong>Whether you have dismissed the storage notice</strong> &mdash; so the '
     'notice does not return on every page.</li></ul>'
     '<p>Both are strictly functional and hold no identifier of any kind. Clearing your '
     'browser data removes them, and the site works exactly the same without them.</p>'),
    ('How we use it',
     '<p>We use the information you send us to answer your enquiry, prepare quotations and '
     'deliver contracted work. We do not sell, rent or trade personal information, and we '
     'do not use it for advertising.</p>'),
    ('Sharing',
     '<p>We share personal information only where it is necessary to perform a contract '
     'with you, or where the law requires it. Where a project involves a federal contract, '
     'we provide the information required by the contracting authority.</p>'),
    ('Retention',
     '<p>Project correspondence is kept for as long as we support the system it relates '
     'to, and for the period required by applicable record-keeping and contracting rules. '
     'Enquiries that do not become projects are removed when they are no longer '
     'useful.</p>'),
    ('Your choices',
     '<p>You may ask what we hold about you, ask us to correct it, or ask us to delete it. '
     'Write to <a href="mailto:acastro@i3automations.com">acastro@i3automations.com</a> and '
     'we will respond. To clear the theme preference, clear site data for this domain in '
     'your browser.</p>'),
    ('Changes',
     '<p>If this policy changes materially, we will publish the revised version on this '
     'page.</p>'),
]

TERMOS = [
    ('Acceptance',
     '<p>By using this website you agree to these terms. If you do not agree with them, '
     'please do not use the site.</p>'),
    ('About the content',
     '<p>The material on this site describes services offered by i3 Automations &amp; '
     'Controls. It is provided for information and does not constitute engineering advice '
     'for any specific installation. No control philosophy, instrument selection or safety '
     'decision should be made on the basis of these pages alone.</p>'),
    ('No offer or contract',
     '<p>Nothing on this site is an offer capable of acceptance. Scope, price, schedule and '
     'liability are established only in a written proposal or contract signed by both '
     'parties.</p>'),
    ('Intellectual property',
     '<p>The text, drawings, photographs, code and design of this site belong to i3 '
     'Automations &amp; Controls unless stated otherwise. Third-party names &mdash; '
     'Rockwell Automation, Siemens, Schneider Electric, Ignition, VTScada, Canary Labs, '
     'AVEVA, Mercedes-Benz, BMW and others &mdash; are the trademarks of their respective '
     'owners and appear here to describe platforms and programs we have worked with.</p>'),
    ('External links',
     '<p>Where we link to another site, we do so for convenience. We do not control those '
     'sites and are not responsible for their content or their privacy practices.</p>'),
    ('Availability',
     '<p>We aim to keep this site available and accurate, but we do not warrant that it '
     'will be uninterrupted or free of error. We may change or withdraw any part of it '
     'without notice.</p>'),
    ('Limitation of liability',
     '<p>To the extent permitted by law, i3 Automations &amp; Controls is not liable for '
     'indirect or consequential loss arising from the use of this website. Nothing here '
     'limits liability that cannot lawfully be limited.</p>'),
    ('Governing law',
     '<p>These terms are governed by the laws of the State of Florida, United States.</p>'),
    ('Contact',
     '<p>Questions about these terms: '
     '<a href="mailto:acastro@i3automations.com">acastro@i3automations.com</a>, or '
     '+1 (407) 820-0299.</p>'),
]


def nao_encontrada():
    """A pagina 404.

    NAO E ENFEITE, e a memoria ja registrava o porque: hospedagem estatica
    (Cloudflare Pages, entre outras) devolve o `index.html` com status **200**
    para qualquer caminho inexistente. Inofensivo numa demo; no dominio real,
    cada URL errada vira uma COPIA DA HOME aos olhos do buscador -- conteudo
    duplicado multiplicado por quantos links quebrados existirem apontando
    para ca.

    Com este arquivo presente, a hospedagem serve ele e devolve 404 de
    verdade. E ele leva `noindex`: pagina de erro indexada e o proprio defeito
    que ela existe para evitar.
    """
    corpo = '''
<section class="secao secao--escura secao--erro">
  <div class="container">
    <div class="bloco reveal">
      <div class="bloco__esq">
        <p class="eyebrow">404</p>
        <h2>This page is not <br>on the drawing</h2>
      </div>
      <div class="bloco__dir">
        <p class="corpo">The link you followed points somewhere that does not exist. The
        work is still here &mdash; start from the capabilities, the record of what already
        runs in the field, or talk to an engineer.</p>
        ''' + cta('capabilities.html', 'All capabilities') + '''
      </div>
    </div>
  </div>
</section>
''' + CONTATO_CTA
    return pagina(
        '404.html', 'Page not found &mdash; i3 Automations &amp; Controls',
        'The page you asked for is not here.', corpo, indexavel=False)


def main():
    feitos = []
    feitos.append(home())
    feitos.append(quem_somos())
    feitos.append(capacidades())
    feitos.append(desempenho())
    feitos.append(servicos())
    feitos.append(galeria())
    feitos.append(contato())
    feitos.append(nao_encontrada())
    feitos.append(legal(
        'privacy-policy.html', 'Privacy Policy &mdash; i3 Automations &amp; Controls',
        'Legal', 'Privacy Policy',
        'What this site collects, what we do with it, and what you can ask us to do about '
        'it.', PRIVACIDADE, 'cabecalho/quem-somos', [1127],
        'Engineers reviewing a control system', 'Privacy Policy'))
    feitos.append(legal(
        'terms-and-conditions.html',
        'Terms and Conditions &mdash; i3 Automations &amp; Controls',
        'Legal', 'Terms and <br>Conditions',
        'The terms that govern the use of this website.', TERMOS,
        'cabecalho/capacidades', [1024], 'Operator at a control room console',
        'Terms and Conditions'))

    # CSS e JS: da fonte comentada para o site/ enxuto. Roda ANTES do
    # relatorio para o total impresso ser o que vai ao ar.
    import build_ativos
    build_ativos.main()
    print('')

    # SEO: sitemap e robots saem do MESMO lugar que as paginas, e nao a mao.
    import datetime
    hoje = datetime.date.today().isoformat()
    # Tres arquivos de deploy, e SO UM deles vale por hospedagem: `.htaccess`
    # em Apache (que e onde este site vai), `_headers`/`_redirects` em
    # Cloudflare Pages ou Netlify. Os inertes nao atrapalham -- e publicar os
    # dois conjuntos e o que faz a troca de hospedagem nao exigir uma entrega.
    for nome, conteudo in (('sitemap.xml', sitemap(hoje)), ('robots.txt', robots()),
                           ('_headers', cabecalhos_deploy()),
                           ('_redirects', redirecionamentos_deploy()),
                           ('.htaccess', htaccess_deploy())):
        caminho = os.path.join(DEST, nome)
        with open(caminho, 'w', encoding='utf-8') as fh:
            fh.write(conteudo)
        feitos.append((caminho, len(conteudo.encode('utf-8'))))

    total = 0
    for caminho, tam in feitos:
        total += tam
        print('   %6.1f KB  %s' % (tam / 1024, os.path.relpath(caminho, DEST)))
    print('')
    print('%d paginas, %.1f KB de HTML.' % (len(feitos), total / 1024))


if __name__ == '__main__':
    main()
