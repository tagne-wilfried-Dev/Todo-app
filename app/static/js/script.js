/* STARFIELD */
(function() {
  const canvas = document.getElementById('starfield');
  const ctx = canvas.getContext('2d');
  let stars = [], W, H;
  function resize() { W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; }
  function initStars() {
    stars = [];
    for (let i = 0; i < 220; i++) {
      stars.push({ x:Math.random()*W, y:Math.random()*H, r:Math.random()*1.2+.2,
        a:Math.random(), speed:Math.random()*.3+.05, twinkle:Math.random()*Math.PI*2 });
    }
  }
  let frame = 0;
  function draw() {
    ctx.clearRect(0,0,W,H);
    frame += .008;
    stars.forEach(s => {
      const alpha = (.4+.6*Math.sin(s.twinkle+frame*s.speed))*s.a;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
      ctx.fillStyle = `rgba(200,220,255,${alpha})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize', () => { resize(); initStars(); });
  resize(); initStars(); draw();
})();

/* DATE */
const now = new Date();
const pad = n => String(n).padStart(2,'0');
document.getElementById('mission-date').textContent =
  `${now.getFullYear()}.${pad(now.getMonth()+1)}.${pad(now.getDate())}`;

function esc(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/* progress-bar*/
let pct = document.getElementById('prog-pct').textContent
console.log(pct)
document.getElementById('prog-fill').style.width = pct;
console.log(document.getElementById('prog-fill').style.width)

/* modal de details des missions */
function openModal(id){
  console.log("modal " +id +" visible");
  document.getElementById("modal"+id).style.opacity = 1
  document.getElementById("modal"+id).style.zIndex = 8
  document.getElementById("modal"+id).style.pointerEvents = 'all'
  document.getElementById("modal-body"+id).style.zIndex = 9 
}
function closeModal(id){
  console.log("modal " +id +" visible");
  document.getElementById("modal"+id).style.opacity = 0
  document.getElementById("modal"+id).style.zIndex = 11  
  document.getElementById("modal"+id).style.pointerEvents = 'none'  
  document.getElementById("modal-body"+id).style.zIndex = 12  
}

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});
function printAllTasks(){
  document.querySelectorAll('.todo-item').forEach(element => {
    element.style.display = 'grid';
  });
}
function printEndedTasks(){
  document.querySelectorAll('.not-ended').forEach(element => {
    element.style.display = 'none';
  });
  document.querySelectorAll('.ended').forEach(element => {
    element.style.display = 'grid';
  });
}
function printPendingTasks(){
  document.querySelectorAll('.ended').forEach(element => {
    element.style.display = 'none';
  });
  document.querySelectorAll('.not-ended').forEach(element => {
    element.style.display = 'grid';
  });
}
