var map = L.map('mapa').setView([-33.485581, -70.697407], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([-33.485581, -70.697407]).addTo(map)
    .bindPopup('¡Estamos aquí!')
    .openPopup();
