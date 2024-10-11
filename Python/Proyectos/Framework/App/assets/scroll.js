document.addEventListener('DOMContentLoaded', function() {
    function scrollToSection(sectionId) {
        console.log("Scrolling to section: " + sectionId);  // Depuración
        document.getElementById(sectionId).scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
    }

    document.getElementById("Sobre_mi_nav").addEventListener("click", function() {
        console.log("Sobre mí clicked");  // Depuración
        scrollToSection("Sobre_mi");
    });

    document.getElementById("Experiencia_nav").addEventListener("click", function() {
        console.log("Experiencia clicked");  // Depuración
        scrollToSection("Experiencia");
    });

    document.getElementById("Certificaciones_nav").addEventListener("click", function() {
        console.log("Certificaciones clicked");  // Depuración
        scrollToSection("Certificaciones");
    });

    document.getElementById("habilidades_nav").addEventListener("click", function() {
        console.log("Habilidades clicked");  // Depuración
        scrollToSection("habilidades");
    });

    document.getElementById("Aportes_nav").addEventListener("click", function() {
        console.log("Aportes clicked");  // Depuración
        scrollToSection("Aportes");
    });
});
