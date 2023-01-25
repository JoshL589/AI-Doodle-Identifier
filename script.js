const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.height = 510;
canvas.width = 510;
ctx.lineWidth = 5;
ctx.strokeStyle = "black";

let painting = false;

canvas.addEventListener("mousedown", startPosition);
canvas.addEventListener("mouseup", finishedPosition);
canvas.addEventListener("mousemove", draw);

function startPosition(e) {
  painting = true;
  draw(e);
}

function finishedPosition() {
  painting = false;
  ctx.beginPath();
}

function draw(e) {
  if (!painting) return;
  ctx.lineWidth = 5;
  ctx.lineCap = "round";
  ctx.stroke();

  ctx.lineTo(e.clientX, e.clientY);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX, e.clientY);
}

const clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clearCanvas);

function clearCanvas() {
  console.log("yo");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
