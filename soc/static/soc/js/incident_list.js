// Function to toggle the display of incident details
function toggleDetails(row) {
    const detailsRow = row.nextElementSibling;
    if (detailsRow.style.display === "none" || detailsRow.style.display === "") {
        detailsRow.style.display = "table-row";
    } else {
        detailsRow.style.display = "none";
    }
}

// Ensure the incident details are initially hidden
document.addEventListener('DOMContentLoaded', function () {
    var detailsRows = document.querySelectorAll('.incident-details');
    detailsRows.forEach(function (row) {
        row.style.display = 'none';
    });
});
