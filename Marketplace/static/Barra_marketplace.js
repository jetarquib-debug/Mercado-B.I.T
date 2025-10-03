
// Obtener los elementos
    const menuButton = document.getElementById('menuButton');
    const menuContainer = document.getElementById('menu');

    // Añadir evento al botón para abrir/cerrar el menú
    menuButton.addEventListener('click', () => {
        // Alternar la clase 'open' para cambiar el estado del menú
        menuContainer.classList.toggle('open');
        // Alternar la clase 'open' en el botón para girar la flecha
        menuButton.classList.toggle('open');
    });