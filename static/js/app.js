document.addEventListener("DOMContentLoaded", () => {
  const firstError = document.querySelector(".field-error");
  if (firstError) {
    firstError.scrollIntoView({ behavior: "smooth", block: "center" });
  }
});
