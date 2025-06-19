let currentSlide = 0;
const slides = document.getElementsByClassName("slide");

function showSlides() {
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].style.display = "block";
    setTimeout(showSlides, 3000); // Change slide every 3 seconds
}

function changeSlide(n) {
    currentSlide = (currentSlide + n + slides.length) % slides.length;
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[currentSlide].style.display = "block";
}

showSlides(); 