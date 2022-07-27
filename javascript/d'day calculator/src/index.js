const title = document.getElementById("title");
const clockTitle = document.querySelector(".js-clock");

const inputForm = document.getElementById("input-form");
const labelDate = document.getElementById("label-date");
const ddayName = document.getElementById("name");
const ddayDate = document.getElementById("date");
const submitBtn = document.querySelector("#input-form input[type='submit']");

const inputContainer = document.getElementById("input-container");
const resultContainer = document.getElementById("result-container");

const againBtn = document.querySelector(".again");
const backBtn = document.querySelector("#input-form input[type='button']");

let interval = null;

if (!localStorage.getItem("name") || !localStorage.getItem("date")) {
  localStorage.setItem("name", "Christmas!");
  localStorage.setItem("date", `${new Date().getFullYear()}-12-25`);
}

function clear(interval) {
  if (interval) {
    clearInterval(interval);
    interval = null;
  }
}

function validCheck(element) {
  const regex = /^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/;
  const value = element.value;

  if (value.length === 0) {
    labelDate.style.color = "black";
    labelDate.innerText = "What date are you waiting for?";
    submitBtn.disabled = true;
    return;
  }

  if (regex.test(value)) {
    labelDate.style.color = "green";
    labelDate.innerText = "What date are you waiting for?    ✔";
    submitBtn.disabled = false;
  } else {
    labelDate.style.color = "tomato";
    labelDate.innerText = "What date are you waiting for?   ❌";
    submitBtn.disabled = true;
  }
}

function calculateDday(name, date) {
  clear(interval);
  const now = new Date();
  const setDate = new Date(date);

  const distance = setDate.getTime() - now.getTime();
  const day = String(Math.floor(distance / (1000 * 60 * 60 * 24)));
  const hours = String(
    Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  ).padStart(2, "0");
  const minutes = String(
    Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))
  ).padStart(2, "0");
  const seconds = String(Math.floor((distance % (1000 * 60)) / 1000)).padStart(
    2,
    "0"
  );
  title.innerText = `Time Until ${name}`;
  clockTitle.innerText = `${day}d ${hours}h ${minutes}m ${seconds}s`;

  interval = setInterval(calculateDday, 1000, name, date);
}

function again() {
  clear(interval);
  title.innerText = "Time Until ...";
  ddayName.value = "";
  ddayDate.value = "";
  validCheck(ddayDate);

  inputContainer.style.display = "block";
  resultContainer.style.display = "none";
}

function back() {
  const name = localStorage.getItem("name");
  const date = localStorage.getItem("date");

  inputContainer.style.display = "none";
  resultContainer.style.display = "block";
  calculateDday(name, date);
}

function handleSubmit(event) {
  event.preventDefault();
  localStorage.setItem("name", ddayName.value);
  localStorage.setItem("date", ddayDate.value);
}

inputForm.addEventListener("submit", handleSubmit);
inputForm.addEventListener("submit", back);
againBtn.addEventListener("click", again);
backBtn.addEventListener("click", back);
