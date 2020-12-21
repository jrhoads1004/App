function createMap(earthquakes, lines) {
    
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 15,
    id: "mapbox.light",
    accessToken: API_KEY
    });
    
    var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 15,
    id: "mapbox.dark",
    accessToken: API_KEY
    });
    
    var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 15,
    id: "mapbox.outdoors",
    accessToken: API_KEY
    });  
       
    airports_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
    var streets = L.tileLayer(airports_url, { attribution });
    // To use OpenStreetMap instead of MapBox
    attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
            
    var titleUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    

    var Stadia_AlidadeSmooth = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png', {
    maxZoom: 20,
    attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });
    // var dayNightLayer = L.terminator();
    var airportIcon = L.icon({
        iconUrl: '../static/images/memphis-international-airport.svg',
        iconSize: [38 / 4, 95 / 4], // size of the icon
      //   popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
      });

    var config = {
        responsive: true,
        displayModeBar: true
    };

    var layers = {
        
        Airports: new L.LayerGroup(),
        DayNight: dayNightLayer,
    };

    var baseMaps = {
    "Light Map": lightmap,
    "Dark Map": darkmap,
    "Outdoor Map": outdoors,
    "Street Map": streets
    };    
    
    
    var map = L.map("map", {
        // For Houston uncomment:
        // center: [31.56, -96.47],
        center: [40.3, -99.14],
        zoom: 4,
        scrollWheelZoom: false, //Disable scroll wheel zoom on Leaflet
        layers: [
          layers.Aircrafts,
          layers.Airports,
          layers.DayNight,
          layers.streets
        ]
      });
      streets.addTo(myMap);

      var overlays = {
        "Aircrafts": layers.Aircrafts,
        "Airports": layers.Airports,
        "Day/Night": layers.DayNight,
        "Street Map": layers.streets
      };
    
    
    L.control.layers(baseMaps, overlays).addTo(myMap);

    
    var info = L.control({
        position: "bottomright"
      });
      
      // When the layer control is added, insert a div with the class of "legend"
      info.onAdd = function (map) {
        var div = L.DomUtil.create("div", "legend");
        return div;
      };
      
    
    // info.onAdd = function (map) {

    //     var div = L.DomUtil.create('div', 'info legend'),
    //         grades = [Infinity, 6, 4.5, 2.5, 1],
    //         labels = [];

    //     for (var i = 0; i < grades.length; i++) {
    //         div.innerHTML +=
    //             '<i style="background:' + color(grades[i] - .1) + '"></i> ' +
    //             grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '>');
    //     }

    //     return div;
    // };
    
    info.addTo(map);
}

d3.json(url).then(function (data) {

    d3.csv("data/airports.csv").then(function (importedData) {
      console.log(importedData);
  
      var airportData = importedData;
      // Cast the data value to a number for each piece of data
      airportData.forEach(function (d) {
        d["Airport ID"] = +d["Airport ID"];
        d["Altitude"] = +d["Altitude"];
        d["Latitude"] = +d["Latitude"];
        d["Longitude"] = +d["Longitude"];
      });
  
      console.log(airportData);
  
      airportData.forEach(function (element) {
        if (element.Country === "United States") {
          var marker = L.circle([element.Latitude, element.Longitude], {
            icon: icons['Airports'],
            fillOpacity: 0.75,
            color: "green",
            fillColor: "black",
            // Adjust: "radius"
            radius: 2000
          }).bindPopup(`<h3>Airport ID: ${element["Airport ID"]}</h3><hr>
                      Airport ID: ${element["Airport ID"]}<br/>
                      Name: ${element["Name"]}<br/>
                      City: ${element["City"]}<br/>
                      Country: ${element["Country"]}<br/>
                      DST: ${element["DST"]}<br/>
                      IATA: ${element["IATA"]}<br/>
                      ICAO: ${element["ICAO"]}<br/>
                      Altitude: ${element["Altitude"]}<br/>
                      Latitude: ${element["Latitude"]}<br/>
                      Longitude: ${element["Longitude"]}<br/>
                      Source: ${element["Source"]}<br/>
                      Timezone: ${element["Timezone"]}<br/>
                      Type: ${element["Type"]}<br/>
                      Tz database time zone: ${element["Tz database time zone"]}<br/>`
          );
          marker.addTo(layers['Airports']);
        }
      });
  
d3.json('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat', marker),