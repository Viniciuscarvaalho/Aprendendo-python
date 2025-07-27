'use strict';

const switcher = document.querySelector('.btn');

switcher.addEventListener('click', function () {
    if (document.body.classList.contains('dark-theme')) {
        document.body.classList.replace('dark-theme', 'light-theme');
        this.textContent = "Dark"; // próximo tema
    } else {
        document.body.classList.replace('light-theme', 'dark-theme');
        this.textContent = "Light"; // próximo tema
    }
});
