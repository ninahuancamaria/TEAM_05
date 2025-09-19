const carusel = document.querySelector('.carousel-track');
const dots = document.querySelector('.carousel-indicator');
const totalSlides = dots.length;
let currentIndex = 0;

function updateCarousel() {
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === currentIndex);
   });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateCarousel();
}

function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
}

updateCarousel();
setInterval(nextSlide, 1000); //cambiar cada 1 segundos
