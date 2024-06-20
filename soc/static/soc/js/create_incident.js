// Initialize Flatpickr for the date picker fields
document.addEventListener('DOMContentLoaded', function () {
    flatpickr(".flatpickr", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
    });
});
