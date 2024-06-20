document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('map').setView([20, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Sample data points
    var dataPoints = [
        [37.7749, -122.4194], // San Francisco
        [51.5074, -0.1278],   // London
        [35.6895, 139.6917]   // Tokyo
    ];

    dataPoints.forEach(function (point) {
        L.circleMarker(point, {
            color: 'red',
            radius: 8
        }).addTo(map);
    });

    // Adjust the map size when the window is resized
    window.addEventListener('resize', function () {
        map.invalidateSize();
    });
});
