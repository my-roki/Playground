import "regenerator-runtime";

const startButton = document.getElementById("start-button");
const audio = document.getElementById("audio");

let stream;
let recorder;
let audioFile;
let recorderTimeout = null;

const init = async () => {
  stream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: false,
  });
  audio.srcObject = stream;
};

const startRecording = () => {
  startButton.innerText = "Stop recording";
  startButton.removeEventListener("click", startRecording);
  startButton.addEventListener("click", stopRecording);

  recorder = new MediaRecorder(stream);
  console.log(recorder);
  recorder.ondataavailable = (event) => {
    audioFile = URL.createObjectURL(event.data);
    audio.srcObject = null;
    audio.src = audioFile;
    audio.play();
  };
  recorder.start();
  recorderTimeout = setTimeout(() => {
    stopRecording();
  }, 5000);
};

const stopRecording = () => {
  if (recorderTimeout) {
    clearTimeout(recorderTimeout);
    recorderTimeout = null;
  }
  startButton.innerText = "Download recording";
  startButton.removeEventListener("click", stopRecording);
  startButton.addEventListener("click", downRecording);

  recorder.stop();
};

function downRecording() {
  const a = document.createElement("a");
  a.href = audioFile;
  a.download = "my_recording.webm";
  document.body.append(a);
  a.click();
}

init();
startButton.addEventListener("click", startRecording);
