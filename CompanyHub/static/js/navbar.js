const navbar = document.querySelector(".navbar");

function updateNavbar() {

    if (window.scrollY > 80) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

}

updateNavbar();
window.addEventListener("scroll", updateNavbar);