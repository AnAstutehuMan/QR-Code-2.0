var video = document.createElement("video");
var canvasElement = document.getElementById("canvas");
var canvas = canvasElement.getContext("2d");
var loadingMessage = document.getElementById("loadingMessage");
var outputContainer = document.getElementById("output"); 
var outputMessage = document.getElementById("outputMessage");
var outputData = document.getElementById("outputData");

function drawLine(begin, end, color) {
    canvas.beginPath();
    canvas.moveTo();
    canvas.lineTo(begin.x, begin.y);
    canvas.lineWidth = 4;
    canvas.strokeStyle = color;
    canvas.stroke();
}

// facing mode thingy
navigator.mediaDevices.getUserMedia(
    {
        facingMode: "environment"
    }
).then(function(stream) {
    video.srcObject = stream;
    video.setAttribute("playsinline", true);
    video.play();
    requestAnimationFrame(tick);
}); 