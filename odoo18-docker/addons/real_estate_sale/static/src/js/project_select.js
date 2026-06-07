/** @odoo-module **/

import { onMounted } from "@odoo/owl";

document.addEventListener('DOMContentLoaded', function () {
    const radios = document.querySelectorAll('input[name="project_id"]');
    const warning = document.getElementById('project-done-warning');

    if (!warning) return;

    // Vérifie si un projet terminé est déjà sélectionné au chargement
    radios.forEach(function (radio) {
        if (radio.checked && radio.dataset.status === 'done') {
            warning.classList.remove('d-none');
        }
    });

    // Écoute les changements
    radios.forEach(function (radio) {
        radio.addEventListener('change', function () {
            const isDone = this.dataset.status === 'done';
            warning.classList.toggle('d-none', !isDone);
        });
    });
});