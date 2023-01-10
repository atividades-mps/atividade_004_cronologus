const root = document.querySelector(".root");
const changeVisualization = document.querySelector(".change-visualization");
const daysDiv = document.querySelector(".days");
const title = document.querySelector(".title");

const weekdays = {
  Sun: 0,
  Mon: 1,
  Tue: 2,
  Wed: 3,
  Thu: 4,
  Fri: 5,
  Sat: 6,
};

function getDays(year, month) {
  const days = [];
  const date = new Date(year, month + 1, 0);
  while (date.getMonth() === month) {
    days.push(new Date(date).getDate());
    date.setDate(date.getDate() - 1);
  }
  return days.reverse();
}

function createDays(date) {
  const pastDays = getDays(
    date.getMonth() - 1 >= 0 ? date.getFullYear() : date.getFullYear() - 1,
    date.getMonth() - 1 >= 0 ? date.getMonth() - 1 : 11
  );

  const year = date.getFullYear();
  const month = date.getMonth();
  let days = getDays(year, month);

  const postDays = getDays(
    date.getMonth() + 1 <= 11 ? date.getFullYear() : date.getFullYear() + 1,
    date.getMonth() + 1 <= 11 ? date.getMonth() + 1 : 0
  );

  const weekday = Intl.DateTimeFormat("en", { weekday: "short" }).format(
    new Date(`${month + 1}-01-${year}`)
  );

  const complementDays = weekdays[weekday];
  const daysLeft = 42 - days.length - complementDays;

  days = [
    ...pastDays.slice(pastDays.length - complementDays),
    ...days,
    ...postDays.slice(0, daysLeft),
  ];

  let weekNumber = 0;

  while (date.getDate() < days[weekNumber]) {
    console.log(weekNumber);
    weekNumber += 7;
  }

  for (let index = weekNumber; index < weekNumber + 7; index++) {
    daysDiv.innerHTML += `
    <div data-date="${month}-${days[index]}-${year}" class="day">
      <label class="day-number">${days[index]}</label>
      <ul class="events"></ul>
    </div>`;
  }
}

function updateCurrentDay(date) {
  let month = Intl.DateTimeFormat("pt-BR", { month: "long" }).format(date);
  title.innerHTML = month[0].toUpperCase() + month.slice(1);
}

function main() {
  const date = root.dataset.date ? new Date(root.dataset.date) : new Date();
  createDays(date);
  updateCurrentDay(date);
  changeVisualization.addEventListener("click", () => {
    redirectTo("/homepage/day");
  });
}

main();
