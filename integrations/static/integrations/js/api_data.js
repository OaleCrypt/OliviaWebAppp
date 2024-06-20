document.addEventListener("DOMContentLoaded", function() {
    // Function to update the Shodan data
    function updateShodanData() {
        fetch('/integrations/shodan/?ip=8.8.8.8')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('shodan-data').innerText = `Error: ${data.error}`;
                } else {
                    document.getElementById('shodan-data').innerHTML = `
                        <p><strong>IP:</strong> ${data.ip_str}</p>
                        <p><strong>Organization:</strong> ${data.org}</p>
                        <p><strong>ISP:</strong> ${data.isp}</p>
                        <p><strong>Country:</strong> ${data.country_name}</p>
                        <p><strong>Last Update:</strong> ${data.last_update}</p>
                        <p><strong>Hostnames:</strong> ${data.hostnames.join(", ")}</p>
                        <p><strong>Ports:</strong> ${data.ports.join(", ")}</p>
                    `;
                }
            })
            .catch(error => {
                document.getElementById('shodan-data').innerText = `Fetch error: ${error}`;
            });
    }

    // Function to update the AbuseIPDB data
    function updateAbuseIPDBData() {
        fetch('/integrations/abuseipdb/?ip=8.8.8.8')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('abuseipdb-data').innerText = `Error: ${data.error}`;
                } else {
                    document.getElementById('abuseipdb-data').innerHTML = `
                        <p><strong>IP Address:</strong> ${data.data.ipAddress}</p>
                        <p><strong>Domain:</strong> ${data.data.domain}</p>
                        <p><strong>Total Reports:</strong> ${data.data.totalReports}</p>
                        <p><strong>ISP:</strong> ${data.data.isp}</p>
                        <p><strong>Country:</strong> ${data.data.countryName}</p>
                        <p><strong>Last Report:</strong> ${data.data.lastReportedAt}</p>
                    `;
                }
            })
            .catch(error => {
                document.getElementById('abuseipdb-data').innerText = `Fetch error: ${error}`;
            });
    }

    // Function to update the GreyNoise data
    function updateGreyNoiseData() {
        fetch('/integrations/greynoise/?ip=8.8.8.8')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('greynoise-data').innerText = `Error: ${data.error}`;
                } else {
                    document.getElementById('greynoise-data').innerHTML = `
                        <p><strong>IP:</strong> ${data.ip}</p>
                        <p><strong>Noise:</strong> ${data.noise}</p>
                        <p><strong>Classification:</strong> ${data.classification}</p>
                        <p><strong>Last Seen:</strong> ${data.last_seen}</p>
                        <p><strong>Link:</strong> <a href="${data.link}">${data.link}</a></p>
                    `;
                }
            })
            .catch(error => {
                document.getElementById('greynoise-data').innerText = `Fetch error: ${error}`;
            });
    }

    // Initial data fetch
    updateShodanData();
    updateAbuseIPDBData();
    updateGreyNoiseData();
});
