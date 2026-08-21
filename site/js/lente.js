/* GERADO por ferramentas/build_ativos.py -- edite fonte/js/lente.js */
(function () {
"use strict";
var reduzido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
var semPonteiro = window.matchMedia("(hover: none)").matches;
var VERTEX = [
"#version 300 es",
"in vec2 pos;",
"out vec2 uv;",
"void main() {",
"  uv = pos * 0.5 + 0.5;",
"  uv.y = 1.0 - uv.y;",
"  gl_Position = vec4(pos, 0.0, 1.0);",
"}"
].join("\n");
var FRAGMENT = [
"#version 300 es",
"precision highp float;",
"in vec2 uv;",
"out vec4 cor;",
"uniform sampler2D uFoto;",
"uniform sampler2D uTraco;",
"uniform vec2  uPonteiro;",
"uniform float uRaio;",
"uniform float uAtivo;",
"uniform float uTempo;",
"uniform float uProporcao;",
"uniform vec2  uEscala;",
"uniform vec2  uDeslocamento;",
"uniform vec3  uTinta;",
"uniform vec3  uPapel;",
"uniform vec3  uAccent;",
"float hash(vec2 p) {",
"  return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123);",
"}",
"float ruido(vec2 p) {",
"  vec2 i = floor(p), f = fract(p);",
"  vec2 u = f * f * (3.0 - 2.0 * f);",
"  return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x),",
"             mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);",
"}",
"float fbm(vec2 p) {",
"  float v = 0.0, a = 0.5;",
"  for (int i = 0; i < 4; i++) { v += a * ruido(p); p *= 2.03; a *= 0.5; }",
"  return v;",
"}",
"void main() {",
"  vec2 iuv = (uv - uDeslocamento) / uEscala;",
"  bool fora = iuv.x < 0.0 || iuv.x > 1.0 || iuv.y < 0.0 || iuv.y > 1.0;",
"  float dist = length((uv - uPonteiro) * vec2(uProporcao, 1.0)) / max(uRaio, 1e-4);",
"  float n = (fbm(uv * 11.0 + uTempo * 0.05) - 0.5) * 0.15;",
"  float mTinta = (1.0 - smoothstep(0.86, 1.04, dist + n)) * uAtivo;",
"  float mPapel = (1.0 - smoothstep(0.74, 0.96, dist + n)) * uAtivo;",
"  float aresta = mTinta * (1.0 - mTinta) * 4.0;",
"  vec2 dir = normalize(uv - uPonteiro + vec2(1e-5));",
"  vec2 iuv2 = iuv - dir * aresta * 0.006 / max(uEscala, vec2(1e-4));",
"  vec4 foto = fora ? vec4(0.0) : texture(uFoto, clamp(iuv2, 0.0, 1.0));",
"  float tinta = fora ? 0.0 : texture(uTraco, clamp(iuv, 0.0, 1.0)).a;",
"  float silhueta = max(foto.a, tinta);",
"  vec3 desenho = mix(uPapel, uTinta, tinta);",
"  float aDesenho = silhueta * max(mPapel, tinta * mTinta);",
"  float aSaida = aDesenho + foto.a * (1.0 - aDesenho);",
"  vec3 cSaida = (desenho * aDesenho + foto.rgb * foto.a * (1.0 - aDesenho))",
"              / max(aSaida, 1e-4);",
"  float t = (dist + n - 0.95) * 26.0;",
"  float banda = exp(-t * t) * uAtivo * silhueta;",
"  cSaida = mix(cSaida, uAccent, clamp(banda * 0.62, 0.0, 1.0));",
"  aSaida = max(aSaida, banda * silhueta * 0.9);",
"  cor = vec4(cSaida, clamp(aSaida, 0.0, 1.0));",
"}"
].join("\n");
function compilar(gl, tipo, fonte) {
var s = gl.createShader(tipo);
gl.shaderSource(s, fonte);
gl.compileShader(s);
if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
console.warn("[lente] shader:", gl.getShaderInfoLog(s));
gl.deleteShader(s);
return null;
}
return s;
}
function rgb(css) {
css = (css || "").trim();
if (css.charAt(0) === "#") {
var h = css.slice(1);
if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
if (h.length >= 6) {
return [parseInt(h.substr(0, 2), 16) / 255,
parseInt(h.substr(2, 2), 16) / 255,
parseInt(h.substr(4, 2), 16) / 255];
}
}
var m = css.match(/-?[\d.]+/g);
if (m && m.length >= 3) return [+m[0] / 255, +m[1] / 255, +m[2] / 255];
return [0, 0.21, 0.4];
}
function carregar(src) {
return new Promise(function (ok, erro) {
var im = new Image();
im.decoding = "async";
im.onload = function () { ok(im); };
im.onerror = erro;
im.src = src;
});
}
function textura(gl, im) {
var t = gl.createTexture();
gl.bindTexture(gl.TEXTURE_2D, t);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, im);
return t;
}
function Lente(el) {
this.el = el;
this.alvo = { x: 0.5, y: 0.5, r: 0, a: 0 };
this.atual = { x: 0.5, y: 0.5, r: 0, a: 0 };
this.raioBase = 0;
this.dentro = false;
this.gl = null;
this.medir();
var self = this;
var ro = window.ResizeObserver ? new ResizeObserver(function () { self.medir(); }) : null;
if (ro) ro.observe(el);
else window.addEventListener("resize", function () { self.medir(); });
if (semPonteiro) {
el.addEventListener("click", function () { el.classList.toggle("is-aberta"); });
return;
}
if (reduzido) {
this.alvo = { x: 0.5, y: 0.5, r: 0.46, a: 1 };
this.atual = { x: 0.5, y: 0.5, r: 0.46, a: 1 };
this.aplicarCSS();
return;
}
el.addEventListener("pointerenter", function () { self.dentro = true; self.alvo.a = 1; });
el.addEventListener("pointerleave", function () { self.dentro = false; self.alvo.a = 0; });
el.addEventListener("pointermove", function (e) {
var c = el.getBoundingClientRect();
if (!c.width) return;
self.alvo.x = (e.clientX - c.left) / c.width;
self.alvo.y = (e.clientY - c.top) / c.height;
self.alvo.a = 1;
self.dentro = true;
}, { passive: true });
}
Lente.prototype.medir = function () {
var c = this.el.getBoundingClientRect();
this.larg = c.width;
this.alt = c.height;
this.raioBase = Math.min(c.width, c.height) * 0.42 / Math.max(c.width, 1);
if (this.canvas) this.ajustarCanvas();
};
Lente.prototype.aplicarCSS = function () {
var s = this.el.style;
s.setProperty("--mx", (this.atual.x * 100).toFixed(2) + "%");
s.setProperty("--my", (this.atual.y * 100).toFixed(2) + "%");
s.setProperty("--r", (this.atual.r * this.larg).toFixed(1) + "px");
};
Lente.prototype.passo = function (dt) {
var a = this.atual, t = this.alvo;
var k = 1 - Math.pow(0.0015, dt);
var kr = 1 - Math.pow(0.004, dt);
a.x += (t.x - a.x) * k;
a.y += (t.y - a.y) * k;
a.a += (t.a - a.a) * kr;
t.r = this.dentro ? this.raioBase : 0;
a.r += (t.r - a.r) * kr;
return a.a > 0.002 || a.r > 0.002;
};
Lente.prototype.iniciarGL = function (canvas, foto, traco, imFoto) {
var gl = canvas.getContext("webgl2", {
alpha: true,
premultipliedAlpha: false,
antialias: false,
depth: false,
stencil: false,
powerPreference: "low-power"
});
if (!gl) return false;
var vs = compilar(gl, gl.VERTEX_SHADER, VERTEX);
var fs = compilar(gl, gl.FRAGMENT_SHADER, FRAGMENT);
if (!vs || !fs) return false;
var p = gl.createProgram();
gl.attachShader(p, vs); gl.attachShader(p, fs); gl.linkProgram(p);
if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
console.warn("[lente] link:", gl.getProgramInfoLog(p));
return false;
}
gl.useProgram(p);
var vao = gl.createVertexArray();
gl.bindVertexArray(vao);
var buf = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, buf);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
var loc = gl.getAttribLocation(p, "pos");
gl.enableVertexAttribArray(loc);
gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
gl.activeTexture(gl.TEXTURE0); textura(gl, foto);
gl.activeTexture(gl.TEXTURE1); textura(gl, traco);
gl.uniform1i(gl.getUniformLocation(p, "uFoto"), 0);
gl.uniform1i(gl.getUniformLocation(p, "uTraco"), 1);
gl.enable(gl.BLEND);
gl.blendFuncSeparate(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA, gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
gl.clearColor(0, 0, 0, 0);
this.gl = gl;
this.prog = p;
this.canvas = canvas;
this.proporcaoImagem = imFoto.naturalWidth / imFoto.naturalHeight;
this.u = {};
["uPonteiro", "uRaio", "uAtivo", "uTempo", "uProporcao", "uEscala",
"uDeslocamento", "uTinta", "uPapel", "uAccent"].forEach(function (n) {
this.u[n] = gl.getUniformLocation(p, n);
}, this);
this.lerTema();
this.ajustarCanvas();
this.el.classList.add("is-gl");
return true;
};
Lente.prototype.lerTema = function () {
var cs = getComputedStyle(this.el);
this.corTinta = rgb(cs.getPropertyValue("--traco"));
this.corPapel = rgb(cs.getPropertyValue("--traco-papel"));
this.corAccent = rgb(cs.getPropertyValue("--dourado") || "#FDC500");
};
Lente.prototype.ajustarCanvas = function () {
if (!this.gl) return;
var dpr = Math.min(window.devicePixelRatio || 1, 2);
var w = Math.max(1, Math.round(this.larg * dpr));
var h = Math.max(1, Math.round(this.alt * dpr));
if (this.canvas.width !== w || this.canvas.height !== h) {
this.canvas.width = w;
this.canvas.height = h;
this.gl.viewport(0, 0, w, h);
}
var cobrir = this.el.classList.contains("lente--retangulo");
var pc = this.larg / Math.max(this.alt, 1);
var pi = this.proporcaoImagem || 1;
var ex, ey;
if (cobrir) {
ex = pi > pc ? pi / pc : 1;
ey = pi > pc ? 1 : pc / pi;
} else {
ex = pi > pc ? 1 : pi / pc;
ey = pi > pc ? pc / pi : 1;
}
this.escala = [ex, ey];
this.deslocamento = [(1 - ex) / 2, (1 - ey) / 2];
this.proporcao = pc;
};
Lente.prototype.desenhar = function (t) {
var gl = this.gl, u = this.u;
gl.useProgram(this.prog);
gl.uniform2f(u.uPonteiro, this.atual.x, this.atual.y);
gl.uniform1f(u.uRaio, this.atual.r);
gl.uniform1f(u.uAtivo, this.atual.a);
gl.uniform1f(u.uTempo, t);
gl.uniform1f(u.uProporcao, this.proporcao);
gl.uniform2fv(u.uEscala, this.escala);
gl.uniform2fv(u.uDeslocamento, this.deslocamento);
gl.uniform3fv(u.uTinta, this.corTinta);
gl.uniform3fv(u.uPapel, this.corPapel);
gl.uniform3fv(u.uAccent, this.corAccent);
gl.clear(gl.COLOR_BUFFER_BIT);
gl.drawArrays(gl.TRIANGLES, 0, 3);
};
var lentes = [];
var rodando = false;
var anterior = 0;
function laco(agora) {
var dt = Math.min((agora - anterior) / 1000, 0.05);
anterior = agora;
var vivo = false;
for (var i = 0; i < lentes.length; i++) {
var L = lentes[i];
if (!L.visivel) continue;
var ativo = L.passo(dt);
if (L.gl) L.desenhar(agora / 1000);
else L.aplicarCSS();
vivo = vivo || ativo;
}
if (vivo) window.requestAnimationFrame(laco);
else rodando = false;
}
function acordar() {
if (rodando) return;
rodando = true;
anterior = performance.now();
window.requestAnimationFrame(laco);
}
function montar(el) {
var L = new Lente(el);
var canvas = el.querySelector(".lente__gl");
var srcFoto = el.getAttribute("data-foto");
var srcTraco = el.getAttribute("data-traco");
lentes.push(L);
L.visivel = true;
if (window.IntersectionObserver) {
var io = new IntersectionObserver(function (ent) {
L.visivel = ent[0].isIntersecting;
if (L.visivel) acordar();
}, { rootMargin: "200px" });
io.observe(el);
}
el.addEventListener("pointerenter", acordar);
el.addEventListener("pointermove", acordar, { passive: true });
el.addEventListener("click", acordar);
if (!canvas || !srcFoto || !srcTraco || !window.WebGL2RenderingContext) {
acordar();
return;
}
Promise.all([carregar(srcFoto), carregar(srcTraco)]).then(function (im) {
try {
if (!L.iniciarGL(canvas, im[0], im[1], im[0])) return;
} catch (e) {
console.warn("[lente] WebGL indisponível, seguindo em CSS:", e);
return;
}
var mm = window.matchMedia("(prefers-color-scheme: dark)");
var relerTema = function () { L.lerTema(); acordar(); };
if (mm.addEventListener) mm.addEventListener("change", relerTema);
document.addEventListener("temachange", relerTema);
acordar();
}).catch(function () { acordar(); });
}
function iniciar() {
var els = document.querySelectorAll("[data-lente]");
for (var i = 0; i < els.length; i++) montar(els[i]);
if (els.length) acordar();
}
if (document.readyState === "loading") {
document.addEventListener("DOMContentLoaded", iniciar);
} else {
iniciar();
}
})();
