/* GERADO por ferramentas/build_ativos.py -- edite fonte/js/marca.js */
(function () {
"use strict";
var G = (typeof globalThis !== "undefined" ? globalThis : window).I3GL;
if (!G) return;
var mult = G.mult, perspectiva = G.perspectiva, olhar = G.olhar;
var rgb = G.rgb, programa = G.programa;
var reduzido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var Z_FUNDO = -34, Z_FRENTE = 34, Z_TELA = 6, Z_GLIFO = 26;
var ESCALA = 100;
var LIMIAR_CANTO = 0.35;
var LIMIAR_RETO = 0.02;
function medirCaminho(el) {
if (!el.getTotalLength || !el.getPointAtLength) return null;
var total = 0;
try { total = el.getTotalLength(); } catch (e) { return null; }
if (!(total > 0)) return null;
return { total: total, n: Math.max(64, Math.min(2400, Math.ceil(total / 1.2))) };
}
function amostrar(el, passo) {
var m = medirCaminho(el);
if (!m) return null;
var bruto = [], i;
for (i = 0; i < m.n; i++) {
var p = el.getPointAtLength(m.total * i / m.n);
bruto.push([p.x, p.y]);
}
return filtrar(bruto, passo);
}
function filtrar(bruto, passo) {
var n = bruto.length, i;
var pts = [], canto = [], acumulado = 1e9;
for (i = 0; i < n; i++) {
var a = bruto[(i - 1 + n) % n], b = bruto[i], c = bruto[(i + 1) % n];
var v1x = b[0] - a[0], v1y = b[1] - a[1];
var v2x = c[0] - b[0], v2y = c[1] - b[1];
var l1 = Math.hypot(v1x, v1y), l2 = Math.hypot(v2x, v2y);
acumulado += l1;
if (l1 < 1e-6 || l2 < 1e-6) continue;
var cruzado = (v1x * v2y - v1y * v2x) / (l1 * l2);
var escalar = (v1x * v2x + v1y * v2y) / (l1 * l2);
var giro = Math.abs(Math.atan2(cruzado, escalar));
if (giro > LIMIAR_CANTO) {
pts.push(b); canto.push(true); acumulado = 0;
} else if (giro > LIMIAR_RETO && acumulado >= passo) {
pts.push(b); canto.push(false); acumulado = 0;
}
}
if (pts.length < 3) return null;
return { pts: pts, canto: canto };
}
function doRetangulo(el) {
var x = parseFloat(el.getAttribute("x")) || 0;
var y = parseFloat(el.getAttribute("y")) || 0;
var w = parseFloat(el.getAttribute("width")) || 0;
var h = parseFloat(el.getAttribute("height")) || 0;
if (!(w > 0 && h > 0)) return null;
return {
pts: [[x, y], [x + w, y], [x + w, y + h], [x, y + h]],
canto: [true, true, true, true]
};
}
function aresta(L, caixa, a, b, peso, tinta) {
L.push(a[0], a[1], a[2], b[0], b[1], b[2], peso, tinta);
for (var i = 0; i < 3; i++) {
caixa[i] = Math.min(caixa[i], a[i], b[i]);
caixa[i + 3] = Math.max(caixa[i + 3], a[i], b[i]);
}
}
function ponto(cx, cy, sx, sy, sz) {
return [(sx - cx) / ESCALA, (cy - sy) / ESCALA, sz / ESCALA];
}
function prisma(L, caixa, cx, cy, forma, z0, z1, peso, tinta) {
var pts = forma.pts, canto = forma.canto, n = pts.length;
var desdeNervura = 0;
for (var i = 0; i < n; i++) {
var a = pts[i], b = pts[(i + 1) % n];
aresta(L, caixa, ponto(cx, cy, a[0], a[1], z0),
ponto(cx, cy, b[0], b[1], z0), peso, tinta);
aresta(L, caixa, ponto(cx, cy, a[0], a[1], z1),
ponto(cx, cy, b[0], b[1], z1), peso, tinta);
desdeNervura++;
if (canto[i] || desdeNervura >= 6) {
aresta(L, caixa, ponto(cx, cy, a[0], a[1], z0),
ponto(cx, cy, a[0], a[1], z1), peso * 0.5, tinta);
desdeNervura = 0;
}
}
}
var PAPEL = {
moldura: { z0: Z_FUNDO, z1: Z_FRENTE, peso: 1.0, tinta: 0, passo: 26 },
tela:    { z0: Z_FUNDO, z1: Z_TELA,   peso: 0.85, tinta: 1, passo: 26 },
glifo:   { z0: Z_TELA,  z1: Z_GLIFO,  peso: 0.85, tinta: 0, passo: 7 }
};
function construir(svg) {
var vb = svg.viewBox && svg.viewBox.baseVal;
var largura = (vb && vb.width) || 410;
var altura = (vb && vb.height) || 258;
var cx = largura / 2, cy = altura / 2;
var L = [], caixa = [1e9, 1e9, 1e9, -1e9, -1e9, -1e9];
var fila = elegiveis(svg);
for (var i = 0; i < fila.length; i++) {
var el = fila[i].el, papel = fila[i].papel;
var forma = (el.tagName.toLowerCase() === "rect")
? doRetangulo(el) : amostrar(el, papel.passo);
if (!forma) continue;
prisma(L, caixa, cx, cy, forma, papel.z0, papel.z1, papel.peso, papel.tinta);
}
return fechar(L, caixa);
}
function elegiveis(svg) {
var fila = [], filhos = svg.querySelectorAll("path, rect");
for (var i = 0; i < filhos.length; i++) {
var el = filhos[i];
if (el.closest && el.closest(".marca__contorno")) continue;
var papel = null, cls = el.getAttribute("class") || "";
for (var nome in PAPEL) {
if (PAPEL.hasOwnProperty(nome) && cls.indexOf(nome) >= 0) {
papel = PAPEL[nome]; break;
}
}
if (papel) fila.push({ el: el, papel: papel });
}
return fila;
}
function fechar(L, caixa) {
if (!L.length) return null;
return { segmentos: new Float32Array(L), caixa: caixa };
}
var ORCAMENTO_MS = 8;
function construirFatiado(svg, pronto) {
var vb = svg.viewBox && svg.viewBox.baseVal;
var largura = (vb && vb.width) || 410;
var altura = (vb && vb.height) || 258;
var cx = largura / 2, cy = altura / 2;
var L = [], caixa = [1e9, 1e9, 1e9, -1e9, -1e9, -1e9];
var fila = elegiveis(svg);
var k = 0, medida = null, bruto = null, j = 0;
function fatia() {
var fim = (window.performance ? performance.now() : Date.now()) + ORCAMENTO_MS;
while (k < fila.length) {
var el = fila[k].el, papel = fila[k].papel, forma = null;
if (el.tagName.toLowerCase() === "rect") {
forma = doRetangulo(el);
} else {
if (!medida) { medida = medirCaminho(el); bruto = []; j = 0; }
if (medida) {
while (j < medida.n) {
var p = el.getPointAtLength(medida.total * j / medida.n);
bruto.push([p.x, p.y]);
j++;
if ((j & 31) === 0 &&
(window.performance ? performance.now() : Date.now()) > fim) {
return window.requestAnimationFrame(fatia);
}
}
forma = filtrar(bruto, papel.passo);
}
medida = null; bruto = null; j = 0;
}
if (forma) {
prisma(L, caixa, cx, cy, forma, papel.z0, papel.z1, papel.peso, papel.tinta);
}
k++;
if ((window.performance ? performance.now() : Date.now()) > fim) {
return window.requestAnimationFrame(fatia);
}
}
pronto(fechar(L, caixa));
}
fatia();
}
var FOV = 0.52, MIRA = 0, AR = 0.96;
var ARCO = 0.80;
var ARCO_ARRASTO = 0.95;
var VS = [
"#version 300 es",
"in vec2 canto;",
"in vec3 pa;",
"in vec3 pb;",
"in float peso;",
"in float tinta;",
"uniform mat4 uMVP;",
"uniform vec2  uEscala;",
"uniform float uFina;",
"uniform float uGrossa;",
"uniform float uDist;",
"uniform float uRaioPeca;",
"out float vPeso;",
"out float vTinta;",
"out float vProf;",
"out vec2  vTela;",
"out float vBorda;",
"out float vMeia;",
"void main() {",
"  vec4 ca = uMVP * vec4(pa, 1.0);",
"  vec4 cb = uMVP * vec4(pb, 1.0);",
"  vec4 c = canto.y < 0.5 ? ca : cb;",
"  vec2 sa = ca.xy / ca.w * uEscala;",
"  vec2 sb = cb.xy / cb.w * uEscala;",
"  vec2 d = sb - sa;",
"  float comp = length(d);",
"  vec2 nrm = comp > 1e-4 ? vec2(-d.y, d.x) / comp : vec2(0.0, 0.0);",
"  float meia = mix(uFina, uGrossa, clamp(peso, 0.0, 1.0)) * 0.5;",
"  vMeia = meia;",
"  vBorda = canto.x * (meia + 0.8);",
"  vec2 s = (canto.y < 0.5 ? sa : sb) + nrm * vBorda;",
"  vec2 ndc = s / uEscala;",
"  gl_Position = vec4(ndc * c.w, c.z, c.w);",
"  vProf = clamp(1.0 - (c.w - (uDist - uRaioPeca)) / (2.0 * uRaioPeca), 0.55, 1.0);",
"  vPeso = peso;",
"  vTinta = tinta;",
"  vTela = ndc * 0.5 + 0.5;",
"}"
].join("\n");
var FS = [
"#version 300 es",
"precision highp float;",
"in float vPeso;",
"in float vTinta;",
"in float vProf;",
"in vec2  vTela;",
"in float vBorda;",
"in float vMeia;",
"uniform vec3  uTinta;",
"uniform vec3  uOuro;",
"uniform vec3  uAceso;",
"uniform float uGanho;",
"uniform vec2  uPonteiro;",
"uniform float uRaio;",
"uniform float uAtivo;",
"uniform float uProp;",
"uniform float uTempo;",
"uniform float uEntrada;",
"out vec4 cor;",
G.RUIDO_GLSL,
"void main() {",
"  vec3 base = mix(uTinta, uOuro, vTinta);",
"  float d = length((vTela - uPonteiro) * vec2(uProp, 1.0)) / max(uRaio, 1e-4);",
"  float n = (fbm(vTela * 9.0 + uTempo * 0.05) - 0.5) * 0.17;",
"  float rev = (1.0 - smoothstep(0.80, 1.04, d + n)) * uAtivo;",
"  float a = (0.55 + 0.45 * vPeso) * uGanho * vProf * uEntrada",
"          * (1.0 + rev * 0.42);",
"  vec3 c = mix(base, uAceso, rev);",
"  float t = (d + n - 0.94) * 20.0;",
"  float banda = exp(-t * t) * uAtivo * uEntrada;",
"  c = mix(c, uAceso, clamp(banda * 0.85, 0.0, 1.0));",
"  a = max(a, banda * vPeso * 0.75);",
"  a *= 1.0 - smoothstep(vMeia - 0.5, vMeia + 0.5, abs(vBorda));",
"  cor = vec4(c, clamp(a, 0.0, 1.0));",
"}"
].join("\n");
function montar(raiz) {
var canvas = raiz.querySelector(".marca3d__tela");
var svg = raiz.querySelector("svg");
if (!canvas || !svg || !window.WebGL2RenderingContext) return;
if (!window.requestAnimationFrame) return;
construirFatiado(svg, function (cena) {
if (cena) comGeometria(raiz, canvas, cena);
});
}
function comGeometria(raiz, canvas, cena) {
var gl = canvas.getContext("webgl2", {
alpha: true, premultipliedAlpha: false, antialias: false,
depth: false, powerPreference: "low-power"
});
if (!gl) return;
var prog = programa(gl, VS, FS, "marca");
if (!prog) return;
var dados = cena.segmentos;
var nSegmentos = dados.length / 8;
var vao = gl.createVertexArray();
gl.bindVertexArray(vao);
var bufQuad = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, bufQuad);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
-1, 0,   1, 0,  -1, 1,
-1, 1,   1, 0,   1, 1
]), gl.STATIC_DRAW);
var aCanto = gl.getAttribLocation(prog, "canto");
gl.enableVertexAttribArray(aCanto);
gl.vertexAttribPointer(aCanto, 2, gl.FLOAT, false, 8, 0);
var bufSeg = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, bufSeg);
gl.bufferData(gl.ARRAY_BUFFER, dados, gl.STATIC_DRAW);
[["pa", 3, 0], ["pb", 3, 12], ["peso", 1, 24], ["tinta", 1, 28]]
.forEach(function (a) {
var loc = gl.getAttribLocation(prog, a[0]);
gl.enableVertexAttribArray(loc);
gl.vertexAttribPointer(loc, a[1], gl.FLOAT, false, 32, a[2]);
gl.vertexAttribDivisor(loc, 1);
});
var CANTOS = [G.cantosDaCaixa(cena.caixa)];
var IDENT = [G.identidade()];
var RAIO = (function () {
var maior = 0.5, p = CANTOS[0];
for (var i = 0; i < 8; i++) {
maior = Math.max(maior, Math.hypot(p[i][0], p[i][1] - MIRA, p[i][2]));
}
return maior;
})();
gl.enable(gl.BLEND);
gl.blendFuncSeparate(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA, gl.ONE,
gl.ONE_MINUS_SRC_ALPHA);
gl.clearColor(0, 0, 0, 0);
var u = {};
["uMVP", "uEscala", "uFina", "uGrossa", "uDist", "uRaioPeca", "uTinta",
"uOuro", "uAceso", "uGanho", "uPonteiro", "uRaio", "uAtivo", "uProp",
"uTempo", "uEntrada"].forEach(function (n) {
u[n] = gl.getUniformLocation(prog, n);
});
var giro = -0.62, giroVel = 0, inclinacao = 0.18, sentido = 1;
var arrastando = false, ultimoX = 0, ultimoY = 0;
var pontX = -9, pontY = -9, ativo = 0, alvoAtivo = 0;
var entrada = 0, dpr = 1, larg = 1, alt = 1;
var corTinta = [0.62, 0.75, 0.88], corOuro = [0.99, 0.77, 0];
var corAceso = [0.99, 0.77, 0], ganho = 0.92;
var fina = 0.9, grossa = 1.8;
var visivel = false, rodando = false, anterior = 0, relogio = 0;
function lerTema() {
var cs = getComputedStyle(raiz);
corTinta = rgb(cs.getPropertyValue("--marca-traco"), [0.62, 0.75, 0.88]);
corOuro = rgb(cs.getPropertyValue("--marca-ouro"), [0.99, 0.77, 0]);
corAceso = rgb(cs.getPropertyValue("--marca-aceso"), corOuro);
ganho = parseFloat(cs.getPropertyValue("--marca-ganho")) || 0.92;
fina = parseFloat(cs.getPropertyValue("--marca-linha-fina")) || 1.4;
grossa = parseFloat(cs.getPropertyValue("--marca-linha-grossa")) || 2.8;
}
var TETO = 4096;
function medir() {
var c = raiz.getBoundingClientRect();
if (c.width < 2 || c.height < 2) return;
dpr = Math.min(window.devicePixelRatio || 1, 2);
larg = Math.min(c.width, TETO / dpr);
alt = Math.min(c.height, TETO / dpr);
var w = Math.round(larg * dpr), h = Math.round(alt * dpr);
if (canvas.width !== w || canvas.height !== h) {
canvas.width = w; canvas.height = h;
gl.viewport(0, 0, w, h);
}
}
var dSuave = 0, dAlvo = 0, enqGiro = 1e9, enqIncl = 1e9, enqProp = 0;
function distanciaDoAngulo() {
var prop = larg / alt;
if (Math.abs(giro - enqGiro) < 0.05 && Math.abs(inclinacao - enqIncl) < 0.05 &&
prop === enqProp) return dAlvo;
enqGiro = giro; enqIncl = inclinacao; enqProp = prop;
dAlvo = G.enquadrarCaixas(CANTOS, IDENT, giro, inclinacao, prop, MIRA, FOV, AR);
return dAlvo;
}
function mvp() {
var alvo = distanciaDoAngulo();
dSuave = dSuave ? dSuave + (alvo - dSuave) * 0.08 : alvo;
var d = dSuave;
var o = [
Math.sin(giro) * Math.cos(inclinacao) * d,
MIRA + Math.sin(inclinacao) * d,
Math.cos(giro) * Math.cos(inclinacao) * d
];
return mult(perspectiva(FOV, larg / alt, 1, 120),
olhar(o, [0, MIRA, 0], [0, 1, 0]));
}
function quadro(agora) {
var dt = Math.min((agora - anterior) / 1000, 0.05);
anterior = agora;
relogio += dt;
if (!arrastando) {
giro += giroVel * dt;
giroVel *= Math.pow(0.02, dt);
if (Math.abs(giroVel) < 0.02 && !reduzido) {
if (giro >= ARCO) sentido = -1;
else if (giro <= -ARCO) sentido = 1;
giro += sentido * 0.022 * dt;
}
if (giro > ARCO_ARRASTO) { giro = ARCO_ARRASTO; giroVel = 0; }
if (giro < -ARCO_ARRASTO) { giro = -ARCO_ARRASTO; giroVel = 0; }
}
entrada += ((visivel ? 1 : 0) - entrada) * (1 - Math.pow(0.02, dt));
ativo += (alvoAtivo - ativo) *
(1 - Math.pow(alvoAtivo > ativo ? 0.002 : 0.06, dt));
medir();
gl.clear(gl.COLOR_BUFFER_BIT);
gl.useProgram(prog);
gl.bindVertexArray(vao);
gl.uniformMatrix4fv(u.uMVP, false, mvp());
gl.uniform3fv(u.uTinta, corTinta);
gl.uniform3fv(u.uOuro, corOuro);
gl.uniform3fv(u.uAceso, corAceso);
gl.uniform1f(u.uGanho, ganho);
gl.uniform2f(u.uEscala, canvas.width / 2, canvas.height / 2);
gl.uniform1f(u.uFina, fina * dpr);
gl.uniform1f(u.uGrossa, grossa * dpr);
gl.uniform1f(u.uDist, dSuave || 12);
gl.uniform1f(u.uRaioPeca, RAIO);
gl.uniform2f(u.uPonteiro, pontX, pontY);
gl.uniform1f(u.uRaio, 0.30);
gl.uniform1f(u.uAtivo, ativo);
gl.uniform1f(u.uProp, larg / alt);
gl.uniform1f(u.uTempo, relogio);
gl.uniform1f(u.uEntrada, entrada);
gl.drawArraysInstanced(gl.TRIANGLES, 0, 6, nSegmentos);
if (visivel || entrada > 0.01) window.requestAnimationFrame(quadro);
else rodando = false;
}
function acordar() {
if (rodando) return;
rodando = true; anterior = performance.now();
window.requestAnimationFrame(quadro);
}
function situar(e) {
var c = raiz.getBoundingClientRect();
pontX = (e.clientX - c.left) / Math.max(1, c.width);
pontY = 1 - (e.clientY - c.top) / Math.max(1, c.height);
}
var campo = (raiz.closest && raiz.closest(".cabecalho")) || raiz;
campo.addEventListener("pointerenter", function () { alvoAtivo = 1; acordar(); });
campo.addEventListener("pointerleave", function () {
if (arrastando) return;
alvoAtivo = 0; acordar();
});
campo.addEventListener("pointermove", function (e) {
if (arrastando) return;
situar(e); alvoAtivo = 1; acordar();
});
raiz.addEventListener("pointerdown", function (e) {
arrastando = true;
ultimoX = e.clientX; ultimoY = e.clientY;
situar(e); alvoAtivo = 1;
if (raiz.setPointerCapture) raiz.setPointerCapture(e.pointerId);
acordar();
});
raiz.addEventListener("pointermove", function (e) {
situar(e); alvoAtivo = 1;
if (arrastando) {
var dx = e.clientX - ultimoX, dy = e.clientY - ultimoY;
ultimoX = e.clientX; ultimoY = e.clientY;
giro = Math.max(-ARCO_ARRASTO,
Math.min(ARCO_ARRASTO, giro - dx * 0.007));
giroVel = -dx * 0.14;
inclinacao = Math.max(-0.9, Math.min(0.9, inclinacao + dy * 0.004));
}
acordar();
});
function soltar(e) {
if (!arrastando) return;
arrastando = false;
if (e && e.pointerId != null && raiz.hasPointerCapture &&
raiz.hasPointerCapture(e.pointerId)) raiz.releasePointerCapture(e.pointerId);
if (window.matchMedia("(hover: none)").matches) alvoAtivo = 0;
acordar();
}
raiz.addEventListener("pointerup", soltar);
raiz.addEventListener("pointercancel", soltar);
raiz.addEventListener("keydown", function (e) {
var passo = 0.18;
if (e.key === "ArrowLeft") giro = Math.max(-ARCO_ARRASTO, giro - passo);
else if (e.key === "ArrowRight") giro = Math.min(ARCO_ARRASTO, giro + passo);
else if (e.key === "ArrowUp") inclinacao = Math.min(0.9, inclinacao + 0.08);
else if (e.key === "ArrowDown") inclinacao = Math.max(-0.9, inclinacao - 0.08);
else return;
e.preventDefault();
pontX = 0.5; pontY = 0.5; alvoAtivo = 1;
acordar();
});
raiz.addEventListener("focus", function () {
pontX = 0.5; pontY = 0.5; alvoAtivo = 1; acordar();
});
raiz.addEventListener("blur", function () { alvoAtivo = 0; acordar(); });
lerTema();
medir();
var mm = window.matchMedia("(prefers-color-scheme: dark)");
if (mm.addEventListener) {
mm.addEventListener("change", function () { lerTema(); acordar(); });
}
document.addEventListener("temachange", function () { lerTema(); acordar(); });
window.addEventListener("resize", function () { medir(); acordar(); });
raiz.setAttribute("tabindex", "0");
raiz.classList.add("is-gl");
if (window.IntersectionObserver) {
new IntersectionObserver(function (ent) {
visivel = ent[0].isIntersecting;
if (visivel) acordar();
}, { rootMargin: "120px" }).observe(raiz);
} else {
visivel = true;
}
acordar();
}
function iniciar() {
var els = document.querySelectorAll("[data-marca3d]");
for (var i = 0; i < els.length; i++) montar(els[i]);
}
if (document.readyState === "loading") {
document.addEventListener("DOMContentLoaded", iniciar);
} else {
iniciar();
}
})();
