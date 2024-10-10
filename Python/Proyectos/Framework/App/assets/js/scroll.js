function scrollToCenter() {
    const target = document.getElementById("Sobre_mi");
    if (target) {
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = targetPosition - (window.innerHeight / 2) + (target.offsetHeight / 2);
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
}