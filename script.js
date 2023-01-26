const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.height = 510;
canvas.width = 510;
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

function draw(e) {
  if (!painting) return;
  ctx.lineWidth = 3;
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
  const predictionh1 = document.getElementById("prediction");
  predictionh1.innerHTML =
    "Prediction: " +
    predictions["predicted_class"] +
    " Confidence: " +
    predictions["confidence"] +
    "%";
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