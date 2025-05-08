document.addEventListener("DOMContentLoaded", function () {
    const cajas = document.querySelectorAll('.caja.animada');

    const mostrarCajas = () => {
        cajas.forEach(caja => {
            const boxTop = caja.getBoundingClientRect().top;
            const triggerBottom = window.innerHeight * 0.85; // Ajusta el umbral

            if (boxTop < triggerBottom) {
                caja.classList.add('visible');
            }
        });
    };

    window.addEventListener('scroll', mostrarCajas);
    mostrarCajas(); // Llamar también al cargar
});