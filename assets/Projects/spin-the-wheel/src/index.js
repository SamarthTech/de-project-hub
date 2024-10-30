const sectors = [
  { color: "#ffd700", text: "#333333", label: "Sweets" },
  { color: "#ff6347", text: "#ffffff", label: "Prize draw" },
  { color: "#4169e1", text: "#ffffff", label: "Extra Spin" },
  { color: "#32cd32", text: "#333333", label: "Big Prize" },
  { color: "#ff69b4", text: "#333333", label: "Sweets + Prize" },
  { color: "#8a2be2", text: "#ffffff", label: "Try Again" },
  { color: "#00ced1", text: "#333333", label: "Gift Voucher" },
  { color: "#ffa500", text: "#333333", label: "You lose" },
];

const prompts = [
  "What's your favorite childhood memory?",
  "If you could travel anywhere, where would you go?",
  "What's the best piece of advice you've ever received?",
  "What's your dream job?",
  "If you could have dinner with any historical figure, who would it be?",
  "What's the most interesting book you've read recently?",
  "If you could have any superpower, what would it be?",
  "What's your favorite way to relax after a long day?",
  "If you could learn any skill instantly, what would it be?",
  "What's the most beautiful place you've ever been to?",
];

const events = {
  listeners: {},
  addListener(eventName, fn) {
    this.listeners[eventName] = this.listeners[eventName] || [];
    this.listeners[eventName].push(fn);
  },
  fire(eventName, ...args) {
    if (this.listeners[eventName]) {
      for (const fn of this.listeners[eventName]) {
        fn(...args);
      }
    }
  },
};

const rand = (min, max) => Math.random() * (max - min) + min;
const tot = sectors.length;
const spinEl = document.querySelector("#spin");
const ctx = document.querySelector("#wheel").getContext("2d");
const dia = ctx.canvas.width;
const rad = dia / 2;
const PI = Math.PI;
const TAU = 2 * PI;
const arc = TAU / sectors.length;

let ang = 0;
let angVel = 0;
let isSpinning = false;  // To ensure only one spin at a time

const getIndex = () => Math.floor(tot - (ang / TAU) * tot) % tot;

function drawSector(sector, i) {
  const ang = arc * i;
  ctx.save();
  ctx.beginPath();
  ctx.fillStyle = sector.color;
  ctx.moveTo(rad, rad);
  ctx.arc(rad, rad, rad, ang, ang + arc);
  ctx.lineTo(rad, rad);
  ctx.fill();
  ctx.translate(rad, rad);
  ctx.rotate(ang + arc / 2);
  ctx.textAlign = "right";
  ctx.fillStyle = sector.text;
  ctx.font = "bold 30px 'Lato', sans-serif";
  ctx.fillText(sector.label, rad - 10, 10);
  ctx.restore();
}

function rotate() {
  const sector = sectors[getIndex()];
  ctx.canvas.style.transform = `rotate(${ang - PI / 2}rad)`;
  if (!angVel) events.fire("rest", sector);
}

function frame() {
  if (!angVel) return;
  angVel *= 0.98;  // Decrement velocity for smooth stop
  if (angVel < 0.002) angVel = 0;  // Stop spinning if velocity is too small
  ang -= angVel;  // Rotate counterclockwise (right to left)
  ang %= TAU;
  rotate();
}

function engine() {
  frame();
  requestAnimationFrame(engine);
}

events.addListener("rest", (sector) => {
  setTimeout(() => {
    const prompt = prompts[Math.floor(rand(0, prompts.length))];
    document.querySelector("#result").textContent = sector.label;
    document.querySelector("#prompt").textContent = prompt;
    openDialog(sector.label);
    spinEl.textContent = "SPIN"; // Reset button text after spin
    spinEl.style.background = "#1e3c72";
    spinEl.style.color = "#fff";
    isSpinning = false;  // Reset spin state
  }, 5000);  // Show result after 5 seconds
});

spinEl.addEventListener("click", () => {
  if (!angVel && !isSpinning) {
    angVel = rand(0.25, 0.35);  // Random velocity for smooth spin
    spinEl.textContent = "SPINNING";
    spinEl.style.background = "#333";
    spinEl.style.color = "#fff";
    isSpinning = true;  // Mark as spinning
  }
});

function openDialog(resultText) {
  const dialog = document.getElementById("resultDialog");
  dialog.style.display = "block";
  document.getElementById("dialogResult").textContent = resultText;
}

function closeDialog() {
  document.getElementById("resultDialog").style.display = "none";
}

sectors.forEach(drawSector);
rotate();
engine();
