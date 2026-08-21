// Fotografa a intro em instantes EXATOS: pausa as animações e busca o tempo.
import { abrirChrome, fecharChrome, Sessao, pagina, avaliar } from "./cdp.mjs";
import { pathToFileURL } from "node:url"; import { resolve } from "node:path";
import { writeFileSync, mkdirSync } from "node:fs";
const L = Number(process.argv[2] || 375), A = Number(process.argv[3] || 667);
const marcas = (process.argv[4] || "250,600,1100,2000,3200,3800").split(",").map(Number);
mkdirSync(resolve("ferramentas/movel/tiras"), { recursive: true });
const ch = await abrirChrome(9395); const br = await Sessao.conectar(ch.browserWs);
const { s, targetId } = await pagina(br, { url: pathToFileURL(resolve("site","index.html")).href, largura: L, altura: A, dpr: 2, movel: true });
console.log(await avaliar(s, `(()=>{const i=document.querySelector('.intro');const c=getComputedStyle(i);
  return 'l1='+c.getPropertyValue('--l1')+' l2='+c.getPropertyValue('--l2');})()`));
// congela tudo o que anima dentro da intro
console.log(await avaliar(s, `(()=>{
  const alvos=[...document.querySelectorAll('.intro, .intro *')];
  window.__an = document.getAnimations().filter(a => a.effect && alvos.includes(a.effect.target));
  window.__an.forEach(a => a.pause());
  return window.__an.map(a=>(a.animationName||'?')+'@'+(a.effect.target.className||a.effect.target.tagName)).join(' | ');
})()`));
for (const m of marcas) {
  await avaliar(s, `(()=>{window.__an.forEach(a=>{try{a.currentTime=${m}}catch(e){}});return 1})()`);
  await new Promise(r => setTimeout(r, 260));
  const { data } = await s("Page.captureScreenshot", { format: "png" });
  writeFileSync(resolve("ferramentas/movel/tiras", `intro-${L}-${String(m).padStart(4,"0")}.png`), Buffer.from(data, "base64"));
}
console.log("ok");
await br.enviar("Target.closeTarget",{targetId}); br.fechar(); fecharChrome(ch);
