// Slideshow funkcionalnost
let currentIndex = 0;
const slides = document.querySelectorAll('.slide');

function changeSlide() {
    slides.forEach(slide => slide.classList.remove('active'));
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add('active');
}

setInterval(changeSlide, 3000); // Sljedeća slika svakih 3 sekunde

// Aktiviraj prvu sliku odmah
changeSlide();
