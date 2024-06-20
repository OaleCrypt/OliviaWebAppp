document.addEventListener('DOMContentLoaded', function () {
    // Hide success or error messages after a few seconds
    setTimeout(function() {
        var messages = document.querySelectorAll('.messages .alert');
        messages.forEach(function (message) {
            message.style.display = 'none';
        });
    }, 1000); 
});
