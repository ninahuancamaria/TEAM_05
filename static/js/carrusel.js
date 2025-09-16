document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".carousel-track");
  const slides = track.querySelectorAll("img");
  let currentIndex = 0;

  function updateCarousel() {
    const offset = currentIndex * track.clientWidth;
    track.style.transform = `translateX(-${offset}px)`;
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  }

  setInterval(nextSlide, 3000); // cambia cada 3 segundos
});
