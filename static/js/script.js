document.addEventListener("DOMContentLoaded", () => {
  const slide = document.querySelector(".slide");
  const items = () => document.querySelectorAll(".item"); // función para obtener los items actualizados

  const $prev = document.getElementById("prev");
  const $next = document.getElementById("next");

  // Botón "prev" → mueve el último al inicio
  $prev.addEventListener("click", () => {
    slide.prepend(items()[items().length - 1]);
  });

  // Botón "next" → mueve el primero al final
  $next.addEventListener("click", () => {
    slide.appendChild(items()[0]);
  });

  // Reproducción automática cada 3 segundos
  setInterval(() => {
    slide.appendChild(items()[0]);
  }, 3000);
});
