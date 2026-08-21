import { abrirChrome, fecharChrome, Sessao } from "../movel/cdp.mjs";
const ch = await abrirChrome(9430);
const b = await Sessao.conectar(ch.browserWs);
const { targetId } = await b.enviar("Target.createTarget", { url: "about:blank" });
const { sessionId } = await b.enviar("Target.attachToTarget", { targetId, flatten: true });
const s = (m, p) => b.enviar(m, p, sessionId);
await s("Page.enable"); await s("Runtime.enable");
await s("Emulation.setDeviceMetricsOverride", { width: 390, height: 844, deviceScaleFactor: 3, mobile: true, screenWidth: 390, screenHeight: 844 });
await s("Emulation.setCPUThrottlingRate", { rate: 4 });
await s("Network.enable");
await s("Network.emulateNetworkConditions", { offline: false, latency: 150, downloadThroughput: 1.6e6/8, uploadThroughput: 750e3/8 });
await s("Page.addScriptToEvaluateOnNewDocument", { source: `
window.__lcp = null;
new PerformanceObserver(l => { for (const e of l.getEntries())
  window.__lcp = { t: Math.round(e.startTime), url: e.url || "(texto)",
                   tag: e.element ? e.element.tagName : "?",
                   cls: e.element ? (e.element.className || "") : "",
                   size: e.size }; }).observe({ type: "largest-contentful-paint", buffered: true });` });
const ok = new Promise(r => { b.on("Page.loadEventFired", r); setTimeout(r, 40000); });
await s("Page.navigate", { url: process.argv[2] }); await ok;
await new Promise(r => setTimeout(r, 3500));
const r = await s("Runtime.evaluate", { expression: "JSON.stringify(window.__lcp)", returnByValue: true });
console.log(JSON.parse(r.result.value));
b.fechar(); fecharChrome(ch);
