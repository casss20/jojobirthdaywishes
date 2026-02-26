import streamlit as st
import streamlit.components.v1 as components

# ─── Page Config ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday JOJO! 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS to remove Streamlit padding ─────────────────────────────
st.markdown("""
<style>
/* Remove default Streamlit padding and UI elements for a full-screen experience */
#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}
div[data-testid="stToolbar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# ─── Improved Canvas Game HTML/JS ─────────────────────────────────────────
html_game = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday Jojo 🌹</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }

:root {
  --rose:    #c0404a;
  --blush:   #f2c4c4;
  --cream:   #fdf6ef;
  --bark:    #2a1a10;
  --sage:    #4a6741;
  --gold:    #c9994a;
  --deep:    #1a0d14;
  --glass:   rgba(253,246,239,0.08);
}

body {
  font-family: 'DM Sans', sans-serif;
  background: var(--deep);
  overflow: hidden;
  height: 100vh;
  width: 100vw;
  cursor: none;
}

/* ── CUSTOM CURSOR ── */
#cursor {
  position: fixed; width:10px; height:10px;
  background: var(--blush); border-radius:50%;
  pointer-events:none; z-index:9999;
  transform: translate(-50%,-50%);
  transition: transform 0.1s ease, background 0.2s;
  mix-blend-mode: difference;
}
#cursor-ring {
  position:fixed; width:32px; height:32px;
  border:1px solid rgba(242,196,196,0.5); border-radius:50%;
  pointer-events:none; z-index:9998;
  transform:translate(-50%,-50%);
  transition: all 0.15s ease;
}

/* ── BACKGROUND CANVAS ── */
#bgCanvas {
  position:fixed; inset:0;
  width:100%; height:100%;
  z-index:0;
}

/* ── BOTANICAL FRAME ELEMENTS ── */
.botanicals {
  position:fixed; inset:0; z-index:1;
  pointer-events:none;
  overflow:hidden;
}

/* SVG rose branch top-left */
.branch-tl {
  position:absolute; top:-40px; left:-60px;
  width:480px; opacity:0.85;
  transform-origin: top left;
  animation: swaySlow 8s ease-in-out infinite;
}
.branch-br {
  position:absolute; bottom:-60px; right:-80px;
  width:520px; opacity:0.8;
  transform: rotate(180deg);
  transform-origin: bottom right;
  animation: swaySlow 9s ease-in-out infinite reverse;
}
@keyframes swaySlow {
  0%,100% { transform:rotate(0deg); }
  50%      { transform:rotate(3deg); }
}

/* ── START SCREEN ── */
#startScreen {
  position:fixed; inset:0; z-index:100;
  display:flex; align-items:center; justify-content:center;
  background: linear-gradient(155deg, #1a0d14 0%, #2d1020 40%, #1a1408 100%);
  transition: opacity 1s ease, transform 1s ease;
}
#startScreen.hide {
  opacity:0; pointer-events:none;
  transform: scale(1.05);
}

.start-inner {
  text-align:center;
  position:relative; z-index:2;
}

.start-eyebrow {
  font-family:'DM Sans', sans-serif;
  font-size:0.7rem; letter-spacing:0.3em;
  color: var(--gold); text-transform:uppercase;
  margin-bottom:24px;
  opacity:0; animation: fadeUp 0.8s ease 0.3s forwards;
}

.start-title {
  font-family:'Cormorant Garamond', serif;
  font-size: clamp(3.5rem, 10vw, 7rem);
  font-weight:300; color: var(--cream);
  line-height:0.95;
  opacity:0; animation: fadeUp 0.9s ease 0.5s forwards;
}
.start-title em {
  font-style:italic; color: var(--blush);
}

.start-sub {
  font-size:0.85rem; letter-spacing:0.15em;
  color: rgba(253,246,239,0.45);
  margin-top:20px; text-transform:uppercase;
  opacity:0; animation: fadeUp 0.8s ease 0.8s forwards;
}

.start-btn {
  margin-top:48px; display:inline-block;
  padding:16px 52px;
  border: 1px solid rgba(242,196,196,0.4);
  background: transparent;
  color: var(--cream); font-family:'DM Sans',sans-serif;
  font-size:0.8rem; letter-spacing:0.25em;
  text-transform:uppercase; cursor:none;
  transition: all 0.4s ease;
  opacity:0; animation: fadeUp 0.8s ease 1.1s forwards;
  position:relative; overflow:hidden;
}
.start-btn::before {
  content:''; position:absolute; inset:0;
  background: linear-gradient(135deg, rgba(192,64,74,0.3), rgba(201,153,74,0.2));
  transform:scaleX(0); transform-origin:left;
  transition: transform 0.4s ease;
}
.start-btn:hover::before { transform:scaleX(1); }
.start-btn:hover {
  border-color: rgba(242,196,196,0.8);
  color: var(--blush);
  box-shadow: 0 0 40px rgba(192,64,74,0.2);
}

/* Decorative lines */
.start-line {
  position:absolute; background: linear-gradient(to right, transparent, rgba(242,196,196,0.3), transparent);
  height:1px; width:300px; left:50%; transform:translateX(-50%);
  opacity:0; animation: fadeIn 1s ease 1.4s forwards;
}
.start-line.top { top:48px; }
.start-line.bot { bottom:48px; }

@keyframes fadeUp {
  from { opacity:0; transform:translateY(24px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeIn {
  from { opacity:0; } to { opacity:1; }
}

/* ── GAME CANVAS ── */
#gameCanvas {
  position:fixed; inset:0;
  width:100%; height:100%;
  z-index:2;
  cursor: none;
}

/* ── HUD ── */
#hud {
  position:fixed; top:0; left:0; right:0;
  z-index:50;
  display:flex; justify-content:space-between; align-items:flex-start;
  padding:28px 40px;
  pointer-events:none;
}

.hud-logo {
  font-family:'Cormorant Garamond',serif;
  font-size:1.1rem; font-weight:300; letter-spacing:0.1em;
  color: rgba(253,246,239,0.5);
}
.hud-logo span { color: var(--blush); }

#progressBar {
  position:fixed; bottom:0; left:0; right:0;
  height:2px; background: rgba(255,255,255,0.06);
  z-index:50; pointer-events:none;
}
#progressFill {
  height:100%;
  background: linear-gradient(to right, var(--rose), var(--gold));
  width:0%; transition: width 0.6s cubic-bezier(0.4,0,0.2,1);
  box-shadow: 0 0 8px rgba(192,64,74,0.8);
}

#roseCount {
  font-family:'DM Sans',sans-serif;
  font-size:0.7rem; letter-spacing:0.2em;
  text-transform:uppercase; color: rgba(253,246,239,0.45);
}
#roseCount strong {
  font-weight:500; color: var(--blush); font-size:1.2rem;
  font-family:'Cormorant Garamond',serif; letter-spacing:0;
}

.hud-bouquet {
  font-size:1.1rem; letter-spacing:4px;
  min-width:120px; text-align:right;
  filter: drop-shadow(0 2px 6px rgba(192,64,74,0.5));
}

/* ── COLLECT FLASH ── */
.collect-flash {
  position:fixed; pointer-events:none;
  z-index:80; font-family:'Cormorant Garamond',serif;
  font-style:italic; font-size:1.2rem;
  color: var(--blush); letter-spacing:0.1em;
  animation: flashUp 1.2s ease forwards;
  text-shadow: 0 2px 10px rgba(192,64,74,0.6);
}
@keyframes flashUp {
  0%   { opacity:0; transform:translateY(0) scale(0.8); }
  20%  { opacity:1; transform:translateY(-10px) scale(1); }
  80%  { opacity:0.8; }
  100% { opacity:0; transform:translateY(-60px) scale(0.9); }
}

/* ── HINT ── */
#hint {
  position:fixed; bottom:40px; left:50%;
  transform:translateX(-50%);
  font-size:0.65rem; letter-spacing:0.25em;
  text-transform:uppercase; color:rgba(253,246,239,0.3);
  z-index:50; pointer-events:none;
  animation: hintPulse 3s ease-in-out infinite;
}
@keyframes hintPulse {
  0%,100% { opacity:0.3; }
  50% { opacity:0.7; }
}

/* ── CELEBRATION ── */
#celebration {
  position:fixed; inset:0; z-index:200;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  background: linear-gradient(155deg, #1a0d14 0%, #2d1020 50%, #1a1408 100%);
  opacity:0; pointer-events:none;
  transition: opacity 1.2s ease;
  overflow-y: auto;
  padding: 60px 0;
}
#celebration.show {
  opacity:1; pointer-events:all;
}

.cel-eyebrow {
  font-size:0.65rem; letter-spacing:0.4em; text-transform:uppercase;
  color: var(--gold); margin-bottom:16px;
  opacity:0;
}
.cel-title {
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(3rem,9vw,6.5rem); font-weight:300;
  color: var(--cream); line-height:0.95;
  text-align:center; letter-spacing:-0.01em;
  opacity:0;
}
.cel-title em {
  font-style:italic;
  background: linear-gradient(135deg, var(--blush), var(--rose), var(--gold));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text;
}

.cel-gift-section {
  text-align: center;
  margin: 24px 0;
  opacity: 0;
}
.cel-gift-text {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  color: rgba(253,246,239,0.5);
  text-transform: uppercase;
  margin-bottom: 24px;
}

.cel-roses {
  font-size:2.2rem; letter-spacing:8px;
  filter: drop-shadow(0 2px 10px rgba(192,64,74,0.4));
}
.cel-divider {
  width:200px; height:1px;
  background: linear-gradient(to right, transparent, rgba(242,196,196,0.5), transparent);
  margin:24px auto; opacity:0;
}
.cel-wish {
  font-family:'Cormorant Garamond',serif;
  font-style:italic; font-size:clamp(1rem,2vw,1.3rem);
  color:rgba(253,246,239,0.7);
  text-align:center; line-height:1.8;
  max-width:680px; padding:0 40px;
  opacity:0;
}

.cel-btn {
  margin-top: 36px;
  padding: 14px 40px;
  background: transparent;
  border: 1px solid rgba(242,196,196,0.3);
  color: var(--blush);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  cursor: none;
  border-radius: 4px;
  transition: all 0.4s ease;
  opacity: 0;
  position: relative;
  overflow: hidden;
}
.cel-btn::before {
  content:''; position:absolute; inset:0;
  background: linear-gradient(135deg, rgba(192,64,74,0.2), rgba(201,153,74,0.1));
  transform:scaleX(0); transform-origin:left;
  transition: transform 0.4s ease;
}
.cel-btn:hover::before { transform:scaleX(1); }
.cel-btn:hover {
  border-color: rgba(242,196,196,0.8);
  box-shadow: 0 0 30px rgba(192,64,74,0.2);
}

.cel-show-1 { animation: fadeUp 0.9s ease 0.2s forwards; }
.cel-show-2 { animation: fadeUp 0.9s ease 0.5s forwards; }
.cel-show-3 { animation: fadeUp 0.9s ease 0.8s forwards; }
.cel-show-4 { animation: fadeUp 0.9s ease 1.1s forwards; }
.cel-show-5 { animation: fadeUp 0.9s ease 1.4s forwards; }
.cel-show-6 { animation: fadeUp 0.9s ease 1.6s forwards; }
.cel-show-7 { animation: fadeUp 0.9s ease 1.9s forwards; }

/* confetti */
.conf {
  position:fixed; pointer-events:none; z-index:210;
  border-radius:2px;
  animation: confDrop linear forwards;
}
@keyframes confDrop {
  from { transform:translateY(-20px) rotate(0deg); opacity:1; }
  to   { transform:translateY(110vh) rotate(900deg); opacity:0; }
}

/* sparkle */
.sparkle-el {
  position:fixed; pointer-events:none; z-index:210;
  font-size:1.2rem;
  animation: sparkFly 1.5s ease forwards;
}
@keyframes sparkFly {
  0%  { transform:translate(0,0) scale(0); opacity:1; }
  50% { opacity:1; }
  100%{ transform:translate(var(--dx),var(--dy)) scale(0.3); opacity:0; }
}
</style>
</head>
<body>

<div id="cursor"></div>
<div id="cursor-ring"></div>

<canvas id="bgCanvas"></canvas>

<!-- Botanical overlays -->
<div class="botanicals">
  <!-- SVG rose branch top-left -->
  <svg class="branch-tl" viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Main stem -->
    <path d="M-20,20 C60,80 120,160 200,220 C280,280 360,300 420,340" stroke="#4a6741" stroke-width="3.5" stroke-linecap="round" fill="none" opacity="0.9"/>
    <!-- Leaves -->
    <ellipse cx="80" cy="105" rx="28" ry="12" fill="#3d5a36" transform="rotate(-35,80,105)" opacity="0.85"/>
    <ellipse cx="155" cy="170" rx="32" ry="13" fill="#4a6741" transform="rotate(-20,155,170)" opacity="0.8"/>
    <ellipse cx="250" cy="245" rx="30" ry="12" fill="#3d5a36" transform="rotate(-10,250,245)" opacity="0.75"/>
    <!-- Rose 1 -->
    <g transform="translate(62,88) rotate(-20)">
      <circle cx="0" cy="0" r="18" fill="#8b1a2a" opacity="0.9"/>
      <circle cx="0" cy="0" r="13" fill="#a82232" opacity="0.9"/>
      <circle cx="0" cy="0" r="8" fill="#c0404a" opacity="1"/>
      <circle cx="-4" cy="-4" r="5" fill="#d45060" opacity="0.7"/>
      <ellipse cx="-7" cy="0" rx="11" ry="7" fill="none" stroke="#8b1a2a" stroke-width="1.5" opacity="0.6" transform="rotate(-30)"/>
      <ellipse cx="7" cy="0" rx="11" ry="7" fill="none" stroke="#8b1a2a" stroke-width="1.5" opacity="0.6" transform="rotate(30)"/>
    </g>
    <!-- Rose 2 -->
    <g transform="translate(200,195) rotate(10)">
      <circle cx="0" cy="0" r="16" fill="#8b1a2a" opacity="0.85"/>
      <circle cx="0" cy="0" r="11" fill="#a82232" opacity="0.9"/>
      <circle cx="0" cy="0" r="7" fill="#c0404a"/>
      <circle cx="-3" cy="-3" r="4" fill="#d45060" opacity="0.7"/>
    </g>
    <!-- Rose 3 bud -->
    <g transform="translate(310,270)">
      <ellipse cx="0" cy="0" rx="8" ry="12" fill="#a82232" opacity="0.8"/>
      <ellipse cx="0" cy="0" rx="5" ry="8" fill="#c0404a" opacity="0.9"/>
    </g>
    <!-- Tiny thorns -->
    <path d="M120,140 L112,132" stroke="#4a6741" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
    <path d="M175,190 L183,182" stroke="#4a6741" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
  </svg>

  <!-- Bottom right mirror branch -->
  <svg class="branch-br" viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M-20,20 C60,80 120,160 200,220 C280,280 360,300 420,340" stroke="#4a6741" stroke-width="3" stroke-linecap="round" fill="none"/>
    <ellipse cx="80" cy="105" rx="28" ry="12" fill="#3d5a36" transform="rotate(-35,80,105)" opacity="0.8"/>
    <ellipse cx="155" cy="170" rx="32" ry="13" fill="#4a6741" transform="rotate(-20,155,170)"/>
    <g transform="translate(62,88) rotate(-20)">
      <circle cx="0" cy="0" r="16" fill="#8b1a2a" opacity="0.85"/>
      <circle cx="0" cy="0" r="11" fill="#a82232" opacity="0.9"/>
      <circle cx="0" cy="0" r="7" fill="#c0404a"/>
    </g>
    <g transform="translate(240,230)">
      <ellipse cx="0" cy="0" rx="8" ry="12" fill="#a82232" opacity="0.75"/>
    </g>
  </svg>
</div>

<!-- START SCREEN -->
<div id="startScreen">
  <div class="start-line top"></div>
  <div class="start-inner">
    <div class="start-eyebrow">A birthday experience</div>
    <div class="start-title">JOJO's<br><em>Garden</em></div>
    <div class="start-sub">Collect the roses · Find the gift</div>
    <button class="start-btn" id="startBtn">Begin →</button>
  </div>
  <div class="start-line bot"></div>
</div>

<!-- GAME CANVAS -->
<canvas id="gameCanvas"></canvas>

<!-- HUD -->
<div id="hud">
  <div class="hud-logo">J<span>.</span>Garden</div>
  <div id="roseCount"><strong id="countNum">0</strong> <span>/ 7 roses</span></div>
  <div class="hud-bouquet" id="bouquetEmojis"></div>
</div>

<div id="progressBar"><div id="progressFill"></div></div>
<div id="hint">click to walk · collect all roses</div>

<!-- CELEBRATION -->
<div id="celebration">
  <div class="cel-eyebrow cel-show-1">With love, always</div>
  <div class="cel-title cel-show-2">Happy<br><em>Birthday,<br>JoJo.</em></div>
  
  <div class="cel-show-3" style="text-align: center; margin: 10px 0; opacity:0; filter: drop-shadow(0 4px 12px rgba(192,64,74,0.3));">
    <canvas id="celGirlCanvas" width="160" height="180"></canvas>
  </div>

  <div class="cel-gift-section cel-show-4">
    <div class="cel-roses" id="celRoses"></div>
  </div>

  <div class="cel-divider cel-show-5"></div>
  <div class="cel-wish cel-show-6">
    Happy Birthday, Jojo! 🎉<br><br>
    Today is all about you, and I just want you to know how truly special you are to me. You bring so much light, love, and joy into my life, and I'm so grateful to have you.<br><br>
    On this beautiful day, I pray that God showers you with every blessing you deserve—happiness, good health, success, love, and so much more. May every door you knock on open wide, and may every dream you carry in your heart come to life.<br><br>
    You deserve the absolute best, Jojo. Never forget how loved and cherished you are.<br><br>
    Happy Birthday—may this year be your greatest one yet. 🌹<br><br>
    With all my love,<br>Anthony 💙
  </div>

  <button class="cel-btn cel-show-7" id="restartBtn">RESTART JOURNEY ↺</button>
</div>

<script>
// ─── CURSOR ───────────────────────────────────────────
const cur = document.getElementById('cursor');
const curRing = document.getElementById('cursor-ring');
let mx=0, my=0;
document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cur.style.left = mx+'px'; cur.style.top = my+'px';
  curRing.style.left = mx+'px'; curRing.style.top = my+'px';
});

// ─── CANVAS SETUP ─────────────────────────────────────
const bgC = document.getElementById('bgCanvas');
const bgX = bgC.getContext('2d');
const gc  = document.getElementById('gameCanvas');
const ctx = gc.getContext('2d');

function resize() {
  bgC.width = gc.width = window.innerWidth;
  bgC.height = gc.height = window.innerHeight;
}
resize();
window.addEventListener('resize', () => { resize(); initFlowers(); });

// ─── PARTICLES / DUST ─────────────────────────────────
const dust = [];
for (let i=0;i<60;i++) dust.push({
  x: Math.random()*window.innerWidth,
  y: Math.random()*window.innerHeight,
  r: Math.random()*1.5+0.3,
  vx:(Math.random()-0.5)*0.3,
  vy:(Math.random()-0.5)*0.3-0.1,
  a: Math.random(),
  da:(Math.random()-0.5)*0.008,
  hue: Math.random()>0.5 ? 350 : 40
});

function drawBg() {
  const W=bgC.width, H=bgC.height;
  // Deep gradient
  const g = bgX.createLinearGradient(0,0,W*0.7,H);
  g.addColorStop(0,'#1a0d14');
  g.addColorStop(0.4,'#200d1a');
  g.addColorStop(0.7,'#1c1408');
  g.addColorStop(1,'#120a0e');
  bgX.fillStyle=g; bgX.fillRect(0,0,W,H);

  // Subtle vignette
  const vig = bgX.createRadialGradient(W/2,H/2,H*0.1,W/2,H/2,H*0.85);
  vig.addColorStop(0,'rgba(0,0,0,0)');
  vig.addColorStop(1,'rgba(0,0,0,0.55)');
  bgX.fillStyle=vig; bgX.fillRect(0,0,W,H);

  // Ground plane
  const gnd = bgX.createLinearGradient(0,H*0.72,0,H);
  gnd.addColorStop(0,'rgba(42,26,16,0)');
  gnd.addColorStop(0.4,'rgba(42,26,16,0.6)');
  gnd.addColorStop(1,'rgba(30,16,10,0.95)');
  bgX.fillStyle=gnd; bgX.fillRect(0,H*0.72,W,H);

  // Ground grass line
  bgX.strokeStyle='rgba(74,103,65,0.25)'; bgX.lineWidth=1;
  bgX.beginPath(); bgX.moveTo(0,H*0.82); bgX.lineTo(W,H*0.82); bgX.stroke();

  // Dust particles
  bgX.save();
  dust.forEach(d=>{
    d.x+=d.vx; d.y+=d.vy;
    d.a+=d.da;
    if(d.a<=0||d.a>=1) d.da*=-1;
    if(d.x<0) d.x=W; if(d.x>W) d.x=0;
    if(d.y<0) d.y=H; if(d.y>H) d.y=0;
    bgX.globalAlpha = Math.max(0,Math.min(1,d.a))*0.4;
    bgX.fillStyle=`hsl(${d.hue},60%,80%)`;
    bgX.beginPath(); bgX.arc(d.x,d.y,d.r,0,Math.PI*2); bgX.fill();
  });
  bgX.restore();
}

// ─── CHARACTER ────────────────────────────────────────
const girl = { x:-80, y:0, tx:-80, ty:0, spd:3.8, dir:1, walk:false, frame:0 };

function drawGirl(t) {
  const x=girl.x, y=girl.y;
  ctx.save();
  ctx.translate(x,y);

  const walk = girl.walk ? Math.sin(t/140)*14 : 0;
  const bob  = girl.walk ? Math.abs(Math.sin(t/140))*-3 : 0;
  ctx.translate(0,bob);
  ctx.scale(girl.dir,1);

  // Shadow
  ctx.save(); ctx.scale(girl.dir,1);
  const sh=ctx.createRadialGradient(0,42,2,0,42,22);
  sh.addColorStop(0,'rgba(0,0,0,0.35)'); sh.addColorStop(1,'rgba(0,0,0,0)');
  ctx.fillStyle=sh; ctx.beginPath(); ctx.ellipse(0,42,22,7,0,0,Math.PI*2); ctx.fill();
  ctx.restore();

  // Legs
  [[-8,walk],[8,-walk]].forEach(([ox,sw])=>{
    ctx.strokeStyle='#e8c4b0'; ctx.lineWidth=9; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(ox,18); ctx.lineTo(ox+sw*0.4,38); ctx.stroke();
    // boot
    const bx=ox+sw*0.4, by=38;
    ctx.fillStyle='#1a0d14';
    ctx.beginPath(); ctx.ellipse(bx+2,by,7,4,0.2,0,Math.PI*2); ctx.fill();
    ctx.fillStyle='#c0404a';
    ctx.beginPath(); ctx.rect(bx-3,by-4,6,4); ctx.fill();
  });

  // Dress
  const dg=ctx.createLinearGradient(0,-15,0,30);
  dg.addColorStop(0,'#e8c4b0'); dg.addColorStop(0.3,'#d4856e'); dg.addColorStop(1,'#a04838');
  ctx.shadowColor='rgba(192,64,74,0.3)'; ctx.shadowBlur=12;
  ctx.fillStyle=dg;
  ctx.beginPath();
  ctx.moveTo(0,-15);
  ctx.bezierCurveTo(22,-5,28,15,26,32);
  ctx.lineTo(-26,32);
  ctx.bezierCurveTo(-28,15,-22,-5,0,-15);
  ctx.fill();
  ctx.shadowBlur=0;

  // Dress detail — belt
  ctx.strokeStyle='rgba(160,72,56,0.6)'; ctx.lineWidth=1;
  ctx.beginPath(); ctx.moveTo(-14,4); ctx.lineTo(14,4); ctx.stroke();

  // Arms
  [[-8,walk*0.6],[8,-walk*0.6]].forEach(([ox,sw])=>{
    ctx.strokeStyle='#e8c4b0'; ctx.lineWidth=8; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(ox,-8); ctx.lineTo(ox+sw,14); ctx.stroke();
  });

  // Head
  ctx.fillStyle='#e8c4b0';
  ctx.beginPath(); ctx.arc(0,-28,16,0,Math.PI*2); ctx.fill();

  // Hair — dark rich brown
  ctx.fillStyle='#1c1010';
  ctx.beginPath(); ctx.arc(0,-31,17,Math.PI*0.75,Math.PI*2.25); ctx.fill();

  // Long hair back
  ctx.fillStyle='#1c1010';
  ctx.beginPath();
  ctx.moveTo(-14,-22);
  ctx.bezierCurveTo(-28,-12,-30+walk*0.15,10,-22+walk*0.15,36);
  ctx.bezierCurveTo(-16,20,-12,5,-10,-18);
  ctx.fill();

  // Hair shine
  ctx.fillStyle='rgba(80,40,20,0.4)';
  ctx.beginPath(); ctx.ellipse(-2,-33,6,3,-0.3,0,Math.PI*2); ctx.fill();

  // Eyes
  ctx.fillStyle='#1a0a18';
  ctx.beginPath(); ctx.ellipse(6,-29,3,3.5,0,0,Math.PI*2); ctx.fill();
  ctx.fillStyle='white';
  ctx.beginPath(); ctx.arc(7,-30,1,0,Math.PI*2); ctx.fill();

  // Lashes
  ctx.strokeStyle='#1a0a18'; ctx.lineWidth=1;
  [[4,-33],[6,-33.5],[8,-33]].forEach(([lx,ly])=>{
    ctx.beginPath(); ctx.moveTo(lx,ly); ctx.lineTo(lx,ly-3); ctx.stroke();
  });

  // Blush
  ctx.fillStyle='rgba(192,64,74,0.25)';
  ctx.beginPath(); ctx.ellipse(11,-24,5,3,0,0,Math.PI*2); ctx.fill();

  // Smile
  ctx.strokeStyle='rgba(140,60,60,0.7)'; ctx.lineWidth=1.2;
  ctx.beginPath(); ctx.arc(3,-23,4,0.1,Math.PI-0.1); ctx.stroke();

  // Hair bow / rose clip
  ctx.fillStyle='#c0404a'; ctx.shadowColor='rgba(192,64,74,0.5)'; ctx.shadowBlur=6;
  ctx.beginPath(); ctx.arc(-13,-34,5,0,Math.PI*2); ctx.fill();
  ctx.fillStyle='#8b1a2a';
  ctx.beginPath(); ctx.arc(-13,-34,3,0,Math.PI*2); ctx.fill();
  ctx.shadowBlur=0;

  ctx.restore();
}

// ─── FLOWERS ──────────────────────────────────────────
const TOTAL = 7;
let flowers=[], collected=0, bouquet=[];

const flowerDefs = [
  {color:'#c0404a',dark:'#8b1a2a',label:'🌹'},
  {color:'#d4607a',dark:'#9b2040',label:'🌷'},
  {color:'#e8a0a0',dark:'#b06060',label:'🌸'},
  {color:'#c84060',dark:'#8a1830',label:'🌹'},
  {color:'#b83050',dark:'#7a1020',label:'🌷'},
  {color:'#e07080',dark:'#a04050',label:'🌸'},
  {color:'#cc5060',dark:'#942030',label:'🌹'},
];

function initFlowers() {
  flowers=[];
  const W=gc.width, H=gc.height;
  const ground=H*0.78;

  for(let i=0;i<TOTAL;i++) {
    let x,y,ok,tries=0;
    do {
      x=120+Math.random()*(W-240);
      y=ground-20+Math.random()*50;
      ok=true;
      if(Math.hypot(x-girl.x,y-girl.y)<140) ok=false;
      flowers.forEach(f=>{ if(Math.hypot(x-f.x,y-f.y)<90) ok=false; });
    } while(!ok && ++tries<120);

    flowers.push({
      x,y,
      def: flowerDefs[i],
      collected:false,
      sc:0, targetSc:0.9+Math.random()*0.25,
      bob: Math.random()*Math.PI*2,
      stem: 18+Math.random()*10,
    });
  }
}

function drawFlower(f,t) {
  if(f.collected) return;
  if(f.sc<f.targetSc) f.sc=Math.min(f.targetSc, f.sc+0.04);

  const bob=Math.sin(t/400+f.bob)*5;
  const {x,y,def,sc,stem}=f;

  ctx.save();
  ctx.translate(x,y+bob);
  ctx.scale(sc,sc);

  // Stem + leaf
  ctx.strokeStyle='#4a6741'; ctx.lineWidth=3; ctx.lineCap='round';
  ctx.beginPath(); ctx.moveTo(0,4); ctx.quadraticCurveTo(3,stem/2,0,stem); ctx.stroke();

  // Leaf
  ctx.fillStyle='#3d5a36';
  ctx.beginPath();
  ctx.save(); ctx.translate(4,stem*0.55); ctx.rotate(-0.5);
  ctx.ellipse(0,0,9,4,0,0,Math.PI*2); ctx.fill(); ctx.restore();

  // Glow
  ctx.shadowColor=def.color; ctx.shadowBlur=18;

  // Outer petals
  ctx.fillStyle=def.dark+'cc';
  for(let i=0;i<6;i++){
    const a=(i/6)*Math.PI*2;
    ctx.beginPath();
    ctx.ellipse(Math.cos(a)*15,Math.sin(a)*15,10,14,a,0,Math.PI*2);
    ctx.fill();
  }
  // Inner petals
  ctx.fillStyle=def.color;
  for(let i=0;i<6;i++){
    const a=(i/6)*Math.PI*2+Math.PI/6;
    ctx.beginPath();
    ctx.ellipse(Math.cos(a)*10,Math.sin(a)*10,7,10,a,0,Math.PI*2);
    ctx.fill();
  }
  // Center
  ctx.fillStyle='#fef3c7'; ctx.shadowColor='#fde68a'; ctx.shadowBlur=10;
  ctx.beginPath(); ctx.arc(0,0,6,0,Math.PI*2); ctx.fill();
  ctx.fillStyle='#fbbf24'; ctx.shadowBlur=0;
  ctx.beginPath(); ctx.arc(0,0,3,0,Math.PI*2); ctx.fill();

  ctx.restore();
}

// ─── GIFT BOX ─────────────────────────────────────────
let giftX=-200, giftTargetX=-200, giftVisible=false, giftOpened=false;

function showGift() {
  giftVisible=true;
  giftTargetX = gc.width - 120;
}

function drawGift(t) {
  if(!giftVisible) return;
  giftX += (giftTargetX-giftX)*0.04;

  const gy = gc.height*0.78 - 5;
  const shake = giftOpened ? 0 : Math.sin(t/80)*3;
  const sc = giftOpened ? 1.6 : 1;

  ctx.save();
  ctx.translate(giftX+shake, gy);
  ctx.scale(sc,sc);

  // Box body
  const bg=ctx.createLinearGradient(0,-25,0,25);
  bg.addColorStop(0,'#8b1a2a'); bg.addColorStop(1,'#5a0d18');
  ctx.fillStyle=bg; ctx.shadowColor='rgba(192,64,74,0.6)'; ctx.shadowBlur=20;
  ctx.beginPath(); ctx.roundRect(-28,-28,56,56,6); ctx.fill();

  // Ribbon vertical
  ctx.fillStyle='#fde68a'; ctx.shadowColor='#fbbf24'; ctx.shadowBlur=8;
  ctx.fillRect(-5,-28,10,56);
  // Ribbon horizontal
  ctx.fillRect(-28,-6,56,12);

  // Bow
  ctx.fillStyle='#fde68a';
  ctx.beginPath(); ctx.ellipse(-12,-28,10,6,-0.5,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.ellipse(12,-28,10,6,0.5,0,Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(0,-28,5,0,Math.PI*2); ctx.fill();

  if(giftOpened) {
    ctx.fillStyle='#fef3c7'; ctx.font='bold 28px serif'; ctx.textAlign='center';
    ctx.fillText('🎉',0,-50);
  }

  ctx.shadowBlur=0;
  ctx.restore();

  // Label
  if(!giftOpened) {
    ctx.save();
    ctx.font='500 11px DM Sans'; ctx.letterSpacing='0.15em';
    ctx.fillStyle='rgba(253,246,239,0.4)'; ctx.textAlign='center';
    ctx.fillText('FOR JOJO ↑', giftX, gy+44);
    ctx.restore();
  }
}

// ─── GROUND GRASS TUFTS ───────────────────────────────
function drawGround(t) {
  const W=gc.width, H=gc.height;
  const gy=H*0.82;

  // Grass tufts
  ctx.strokeStyle='rgba(74,103,65,0.5)'; ctx.lineWidth=1.5; ctx.lineCap='round';
  for(let i=0;i<W;i+=18) {
    const sw=Math.sin(t/600+i*0.1)*2;
    ctx.beginPath(); ctx.moveTo(i,gy); ctx.lineTo(i+sw-2,gy-8); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(i+5,gy); ctx.lineTo(i+5+sw,gy-11); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(i+10,gy); ctx.lineTo(i+10+sw+1,gy-7); ctx.stroke();
  }
}

// ─── SCORE HUD ────────────────────────────────────────
function updateHUD() {
  document.getElementById('countNum').textContent = collected;
  document.getElementById('progressFill').style.width = (collected/TOTAL*100)+'%';
  document.getElementById('bouquetEmojis').textContent = bouquet.join('');
}

// ─── COLLECT ──────────────────────────────────────────
const collectWords = ['LOVE', 'PROSPERITY', 'JOY', 'HEALTH', 'SUCCESS', 'PEACE', 'HAPPINESS'];

function collectFlower(f) {
  f.collected=true; collected++; bouquet.push('🌹');

  // Sparkle burst
  for(let i=0;i<10;i++){
    const sp=document.createElement('div');
    sp.className='sparkle-el';
    const angle=Math.random()*Math.PI*2;
    const dist=50+Math.random()*80;
    sp.style.cssText=`left:${f.x}px;top:${f.y}px;--dx:${Math.cos(angle)*dist}px;--dy:${Math.sin(angle)*dist}px`;
    sp.textContent=['✦','✧','·','*','⁎'][Math.floor(Math.random()*5)];
    sp.style.color=f.def.color;
    document.body.appendChild(sp);
    setTimeout(()=>sp.remove(),1500);
  }

  // Flash text
  const fl=document.createElement('div');
  fl.className='collect-flash';
  fl.style.left=f.x+'px'; fl.style.top=(f.y-30)+'px';
  fl.textContent=collectWords[collected - 1] || '+1 rose';
  document.body.appendChild(fl);
  setTimeout(()=>fl.remove(),1200);

  updateHUD();

  if(collected===TOTAL) {
    setTimeout(showGift, 500);
    document.getElementById('hint').style.opacity = '1';
    document.getElementById('hint').textContent='🎁 walk to the gift →';
  }
}

// ─── OPEN GIFT ────────────────────────────────────────
let celebrationDone=false;
function openGift() {
  if(celebrationDone) return;
  celebrationDone=true;
  giftOpened=true;

  document.getElementById('celRoses').textContent = bouquet.join('');
  setTimeout(()=>{
    document.getElementById('celebration').classList.add('show');
    launchConfetti();
    setTimeout(launchConfetti,2500);
    setTimeout(launchConfetti,5000);
    document.getElementById('hint').style.opacity='0';
  }, 600);
}

function launchConfetti() {
  const colors=['#c0404a','#fde68a','#e8c4b0','#4a6741','#8b1a2a','#f2c4c4'];
  for(let i=0;i<70;i++){
    const c=document.createElement('div');
    c.className='conf';
    c.style.left=Math.random()*100+'vw';
    c.style.top='-10px';
    c.style.width=(5+Math.random()*7)+'px';
    c.style.height=(5+Math.random()*7)+'px';
    c.style.background=colors[Math.floor(Math.random()*colors.length)];
    c.style.borderRadius=Math.random()>0.5?'50%':'2px';
    c.style.animationDuration=(2.5+Math.random()*3)+'s';
    c.style.animationDelay=(Math.random()*2)+'s';
    document.body.appendChild(c);
    setTimeout(()=>c.remove(),5500);
  }
}

// ─── GAME LOOP ────────────────────────────────────────
let running=false, t=0;

// ─── CELEBRATION GIRL ─────────────────────────────────
const celCanvas = document.getElementById('celGirlCanvas');
const celCtx = celCanvas ? celCanvas.getContext('2d') : null;

function drawCelGirl(t) {
  if (!celCtx) return;
  const cx = celCtx;
  cx.clearRect(0,0,160,180);
  cx.save();
  cx.translate(80, 110);
  const bob = Math.sin(t/300)*3;
  cx.translate(0, bob);
  cx.scale(1.4, 1.4);

  // Shadow
  cx.save();
  const sh=cx.createRadialGradient(0,42,2,0,42,22);
  sh.addColorStop(0,'rgba(0,0,0,0.3)'); sh.addColorStop(1,'rgba(0,0,0,0)');
  cx.fillStyle=sh; cx.beginPath(); cx.ellipse(0,42-bob,22,7,0,0,Math.PI*2); cx.fill();
  cx.restore();

  // Legs
  cx.strokeStyle='#e8c4b0'; cx.lineWidth=9; cx.lineCap='round';
  cx.beginPath(); cx.moveTo(-8,18); cx.lineTo(-8,38); cx.stroke();
  cx.beginPath(); cx.moveTo(8,18); cx.lineTo(8,38); cx.stroke();
  cx.fillStyle='#1a0d14'; // boots
  cx.beginPath(); cx.ellipse(-6,38,7,4,0,0,Math.PI*2); cx.fill();
  cx.beginPath(); cx.ellipse(10,38,7,4,0,0,Math.PI*2); cx.fill();
  cx.fillStyle='#c0404a';
  cx.beginPath(); cx.rect(-11,34,6,4); cx.fill();
  cx.beginPath(); cx.rect(5,34,6,4); cx.fill();

  // Dress
  const dg=cx.createLinearGradient(0,-15,0,30);
  dg.addColorStop(0,'#e8c4b0'); dg.addColorStop(0.3,'#d4856e'); dg.addColorStop(1,'#a04838');
  cx.shadowColor='rgba(192,64,74,0.3)'; cx.shadowBlur=12;
  cx.fillStyle=dg;
  cx.beginPath();
  cx.moveTo(0,-15);
  cx.bezierCurveTo(25,-5,32,15,30,32);
  cx.lineTo(-30,32);
  cx.bezierCurveTo(-32,15,-25,-5,0,-15);
  cx.fill();
  cx.shadowBlur=0;
  
  // Belt
  cx.strokeStyle='rgba(160,72,56,0.6)'; cx.lineWidth=1;
  cx.beginPath(); cx.moveTo(-16,4); cx.lineTo(16,4); cx.stroke();

  // Head
  cx.fillStyle='#e8c4b0';
  cx.beginPath(); cx.arc(0,-28,16,0,Math.PI*2); cx.fill();

  // Hair back
  cx.fillStyle='#1c1010';
  cx.beginPath(); cx.arc(0,-31,17,Math.PI*0.75,Math.PI*2.25); cx.fill();
  
  // Long hair
  cx.beginPath();
  cx.moveTo(-16,-22);
  cx.bezierCurveTo(-32,-12,-34,10,-24,36);
  cx.bezierCurveTo(-18,20,-14,5,-12,-18);
  cx.fill();
  cx.beginPath();
  cx.moveTo(16,-22);
  cx.bezierCurveTo(32,-12,34,10,24,36);
  cx.bezierCurveTo(18,20,14,5,12,-18);
  cx.fill();

  // Shine
  cx.fillStyle='rgba(80,40,20,0.4)';
  cx.beginPath(); cx.ellipse(-5,-33,6,3,-0.2,0,Math.PI*2); cx.fill();
  cx.beginPath(); cx.ellipse(5,-33,6,3,0.2,0,Math.PI*2); cx.fill();

  // Eyes (happy closed)
  cx.strokeStyle='#1a0a18'; cx.lineWidth=1.5;
  cx.beginPath(); cx.arc(-5,-28,4,Math.PI,Math.PI*2); cx.stroke();
  cx.beginPath(); cx.arc(5,-28,4,Math.PI,Math.PI*2); cx.stroke();

  // Blush
  cx.fillStyle='rgba(192,64,74,0.4)';
  cx.beginPath(); cx.ellipse(-8,-24,5,3,0,0,Math.PI*2); cx.fill();
  cx.beginPath(); cx.ellipse(8,-24,5,3,0,0,Math.PI*2); cx.fill();

  // Smile
  cx.strokeStyle='rgba(140,60,60,0.8)'; cx.lineWidth=1.5;
  cx.beginPath(); cx.arc(0,-25,5,0.1,Math.PI-0.1); cx.stroke();
  cx.fillStyle='rgba(140,60,60,0.8)';
  cx.beginPath(); cx.arc(0,-25,5,0,Math.PI); cx.fill();

  // Arms holding bouquet
  cx.strokeStyle='#e8c4b0'; cx.lineWidth=8; cx.lineCap='round';
  cx.beginPath(); cx.moveTo(-10,-8); cx.lineTo(-4,8); cx.stroke();
  cx.beginPath(); cx.moveTo(10,-8); cx.lineTo(4,8); cx.stroke();

  // Bouquet
  cx.font = '28px serif';
  cx.textAlign='center';
  cx.fillText('💐', 0, 15);

  cx.restore();
}

function setTarget(e) {
  if(!running) return;
  const r=gc.getBoundingClientRect();
  let cx,cy;
  if(e.touches){ cx=e.touches[0].clientX; cy=e.touches[0].clientY; }
  else { cx=e.clientX; cy=e.clientY; }
  girl.tx = Math.max(40, Math.min(gc.width-40, cx-r.left));
  girl.ty = Math.max(gc.height*0.55, Math.min(gc.height*0.88, cy-r.top));
}

gc.addEventListener('click', setTarget);
gc.addEventListener('mousemove', e=>{ if(e.buttons===1) setTarget(e); });
gc.addEventListener('touchstart', e=>{e.preventDefault();setTarget(e);},{passive:false});
gc.addEventListener('touchmove', e=>{e.preventDefault();setTarget(e);},{passive:false});

// Place girl initially
function placeGirl() {
  girl.x = 100;
  girl.y = gc.height*0.8;
  girl.tx = 100; girl.ty = girl.y;
}

function loop() {
  if(!running) return;
  t = performance.now();
  drawBg();

  ctx.clearRect(0,0,gc.width,gc.height);

  // Move girl
  const dx=girl.tx-girl.x, dy=girl.ty-girl.y, dist=Math.hypot(dx,dy);
  if(dist>4){
    girl.walk=true; girl.frame++;
    girl.x+=dx/dist*girl.spd;
    girl.y+=dy/dist*girl.spd;
    girl.dir=dx>0?1:-1;
  } else { girl.walk=false; }

  // Check flowers
  flowers.forEach(f=>{
    if(!f.collected && Math.hypot(girl.x-f.x,girl.y-f.y)<48) collectFlower(f);
  });

  // Check gift
  if(giftVisible&&!celebrationDone&&Math.abs(girl.x-giftX)<60&&Math.abs(girl.y-(gc.height*0.78))<50&&collected===TOTAL) {
    openGift();
  }

  drawGround(t);

  // Draw flowers behind girl if above, in front if below
  const gY=girl.y;
  flowers.filter(f=>!f.collected&&f.y<gY).forEach(f=>drawFlower(f,t));
  drawGift(t);
  drawGirl(t);
  flowers.filter(f=>!f.collected&&f.y>=gY).forEach(f=>drawFlower(f,t));

  if (celebrationDone) {
    drawCelGirl(t);
  }

  requestAnimationFrame(loop);
}

// Start button
document.getElementById('startBtn').addEventListener('click',()=>{
  document.getElementById('startScreen').classList.add('hide');
  setTimeout(()=>{
    running=true;
    placeGirl();
    initFlowers();
    updateHUD();
    loop();
  },900);
});

// Restart button
document.getElementById('restartBtn').addEventListener('click', () => {
  // Reset game state
  collected = 0;
  bouquet = [];
  celebrationDone = false;
  giftVisible = false;
  giftOpened = false;
  giftX = -200;
  giftTargetX = -200;
  
  // Hide celebration
  document.getElementById('celebration').classList.remove('show');
  
  // Reset hud
  updateHUD();
  
  // Re-init flowers
  initFlowers();
  
  // Reposition girl
  placeGirl();

  // Hint
  document.getElementById('hint').style.opacity = '1';
  document.getElementById('hint').textContent = 'click to walk · collect all roses';
  
  // Return to start screen
  document.getElementById('startScreen').classList.remove('hide');
  running = false;
  
  // Start ambient bg again
  ambientBg();
});

// Ambient bg before start
(function ambientBg(){
  if(!running){ drawBg(); requestAnimationFrame(ambientBg); }
})();
</script>
</body>
</html>
"""

# Embed the HTML game so it fills the screen height automatically mapping to 100vh
components.html(html_game, height=850, scrolling=False)
