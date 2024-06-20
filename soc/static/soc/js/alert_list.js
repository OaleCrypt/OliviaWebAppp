// Function to toggle the display of alert details
function toggleDetails(row) {
    const detailsRow = row.nextElementSibling;
    if (detailsRow.style.display === "none" || detailsRow.style.display === "") {
        detailsRow.style.display = "table-row";
    } else {
        detailsRow.style.display = "none";
    }
}

// Ensure the alert details are initially hidden
document.addEventListener('DOMContentLoaded', function () {
    var detailsRows = document.querySelectorAll('.alert-details');
    detailsRows.forEach(function (row) {
        row.style.display = 'none';
    });

    // Hide success or error messages after a few seconds
    setTimeout(function() {
        var messages = document.querySelectorAll('.messages .alert');
        messages.forEach(function (message) {
            message.style.display = 'none';
        });
    }, 2000); // Hide after 2 seconds
});
