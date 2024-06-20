document.addEventListener('DOMContentLoaded', function () {
    // Initialize Flatpickr for the date picker fields with the class 'flatpickr'
    flatpickr(".flatpickr", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
    });
});
