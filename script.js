const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.height = 560;
canvas.width = 560;

ctx.strokeStyle = "black";
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

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

var left = canvas.offsetLeft;
var top = canvas.offsetTop;

function draw(e) {
  if (!painting) return;
  ctx.lineWidth = 3;
  ctx.lineCap = "round";
  ctx.stroke();

  ctx.lineTo(e.clientX - left - 10, e.clientY - top - 10);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX - left - 10, e.clientY - top - 10);
}

const clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clearCanvas);

function clearCanvas() {
  console.log("yo");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// predict function that takes the image in canvas and turns it into a 28x28 image

const predictButton = document.getElementById("predict");
predictButton.addEventListener("click", predict);

// Use the Fetch API to send the image data to the backend
async function predict() {
  // Get the image data from the canvas
  const canvas = document.getElementById("canvas");
  const imageData = canvas.toDataURL("image/png");
  console.log(imageData);
  // Convert the image data to a blob
  const blob = await fetch(imageData).then((response) => response.blob());
  // Create a FormData object to send the image data
  const formData = new FormData();
  formData.append("image", blob, "image.png");
  console.log(formData);
  // Send the image data to the backend
  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData,
  });
  // Get the prediction results from the response
  const predictions = await response.json();
  // Do something with the predictions
  console.log(predictions);

  const class_names = [
    "bee",
    "bowtie",
    "butterfly",
    "cat",
    "diamond",
    "eye",
    "mushroom",
    "octopus",
    "popsicle",
    "snowman",
  ];

  for (let i = 0; i < class_names.length; i++) {
    const predictionLi = document.getElementById(class_names[i]);
    const predictionLitag = document.getElementById(class_names[i] + "tag");
    predictionLi.innerHTML = `${predictions["predictions"][i]["confidence"]}`;
    predictionLi.style.color = "white";
    predictionLitag.style.color = "white";
  }

  const correct = predictions["predicted_class"];

  const correctLi = document.getElementById(correct);
  const correctLitag = document.getElementById(correct + "tag");
  correctLi.style.color = "#3CB371";
  correctLitag.style.color = "#3CB371";
}

const class_names = [
  "bee",
  "bowtie",
  "butterfly",
  "cat",
  "diamond",
  "eye",
  "mushroom",
  "octopus",
  "popsicle",
  "snowman",
];
