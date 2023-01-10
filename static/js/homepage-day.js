const root = document.querySelector(".root");
const daysDiv = document.querySelector(".days");
const title = document.querySelector(".title");
const changeVisualization = document.querySelector(".change-visualization");
const weekTitle = document.querySelector(".weekday");

const weekdays = {
  Sun: 0,
  Mon: 1,
  Tue: 2,
  Wed: 3,
  Thu: 4,
  Fri: 5,
  Sat: 6,
};

function createDays(date) {
  daysDiv.innerHTML += `
  <div class="day">
  <label class="day-number">${date.getDate()}</label>
  <ul class="events"></ul>
  </div>`;
}

function updateCurrentDay(date) {
  let day = Intl.DateTimeFormat("pt-BR", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(date);
  title.innerHTML = day[0].toUpperCase() + day.slice(1);

  const week = Intl.DateTimeFormat("pt-BR", {
    weekday: "long",
  }).format(date);

  weekTitle.innerHTML = week[0].toUpperCase() + week.slice(1);
}

function main() {
  const date = root.dataset.date ? new Date(root.dataset.date) : new Date();
  createDays(date);
  updateCurrentDay(date);
  changeVisualization.addEventListener("click", () => {
    redirectTo("/homepage/month");
  });
}

main();
