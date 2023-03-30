function initMap() {
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: {lat:1.2790, lng: 103.8545}
    });

    directionsRenderer.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsRenderer);
    document.getElementById("submitBtn").addEventListener("click", () => {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    })
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    const selectedMode = "DRIVING";

    directionsService.route({
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,

        travelMode: google.maps.TravelMode[selectedMode]
    })
    .then((response) => {
        directionsRenderer.setDirections(response);
    })
    // .catch((e) => window.alert("Direction request failed"));
}