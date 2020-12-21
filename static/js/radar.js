
 var myMap = L.map("map", {
    // center: [39, -99],
    // zoom: 4,
    center: [16, 0],
    zoom: 2,
    layers: [OpenStreetTiles, airportLayer, aircraftsLayer],
    scrollWheelZoom: false //Disable scroll wheel zoom on Leaflet
});

// Create a layer control
// Pass in our baseMaps and overlayMaps
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
    collapsed: false,

    attribution:
        'Map data &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    leafletRadarAttribution:
        '<a href="https://github.com/rwev/leaflet-radar">Radar</a>';

    OpenStreetTiles: L.tileLayer(
            "https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png",
                    {
                        attribution: [
                        osmAttribution,
                        leafletRadarAttribution
                                            ].join(" | ")
                                }
    )}.addTo(myMap);
L.control.radar({}).addTo(map);