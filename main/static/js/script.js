window.onscroll = function () {
    var navbar = document.querySelector('.navbar');
    if (window.pageYOffset > 50) { // Când se dă scroll peste 50px
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
};
// Capture selected values on change
document.getElementById("judet").addEventListener("change", function () {
    console.log("Selected Judetul:", this.value);
});

document.getElementById("balti").addEventListener("change", function () {
    console.log("Selected Balti:", this.value);
});

document.getElementById("pret").addEventListener("change", function () {
    console.log("Selected Pret:", this.value);
});
