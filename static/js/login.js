const form = document.querySelector(".form");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const login = parseForm(form);
  fetch("/login", {
    method: "POST",
    body: login,
  });
  redirectTo("/homepage");
});
