import "regenerator-runtime";

const startButton = document.getElementById("start-button");
const audio = document.getElementById("audio");

const init = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: false,
  });
};

const startRecording = () => {
  //   audio.srcObject = stream;
  //   audio.autoplay = true;

  startButton.innerText = "Stop recording";
  startButton.removeEventListener("click", startRecording);
  startButton.addEventListener("click", stopRecording);
};

const stopRecording = () => {
  startButton.innerText = "Start recording";
  startButton.removeEventListener("click", stopRecording);
  startButton.addEventListener("click", startRecording);
};

init();
startButton.addEventListener("click", startRecording);
