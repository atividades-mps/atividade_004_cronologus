function parseForm(form) {
  let formData = {};
  for (const [key, value] of new FormData(form)) {
    formData[key] = value;
  }
  return formData;
}

function redirectTo(to) {
  window.location = to;
}
