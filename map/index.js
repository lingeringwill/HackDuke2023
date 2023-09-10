let map;
let points = [];

var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyApBGLyOG3tTnJsCjj1_vDeimFp72_xF0Y&libraries=visualization&callback=initMap';
script.async = true;

window.initMap = async function() {
    const { Map } = await google.maps.importLibrary("maps");

    await fetch("points.json")
      .then((response) => response.json())
      .then((json) => loadPoints(json))

    async function loadPoints(json) {
        for (let i = 0; i < json.length; i++) {
            points.push(new Array());
            for (let j = 0; j < json[i].length; j++) {
                let obj = json[i][j];
                points[i].push({location: new google.maps.LatLng(obj["location"]["lat"], obj["location"]["lng"]), weight: obj["weight"]}) // finish this
            }
        }
    }     

    // bigger weight = more red
    var US = new google.maps.LatLng(37, -95);
  
    map = new Map(document.getElementById("map"), {
      center: US,
      zoom: 5,
      disableDefaultUI: true,
      fullscreenControl: true,
    });

    const gradient = [
        "rgba(0, 0, 0, 0)",
        "rgba(255, 100, 0, 0.4)",
        "rgba(255, 165, 0, 0.65)",
        "rgba(255, 210, 0, 0.85)",
        "rgba(255, 0, 0, 1)",
    ];

    var heatmap = new google.maps.visualization.HeatmapLayer({
      data: points[0],
      radius: 0.3,
      maxIntensity: 100,
      dissipating: false,
      gradient: gradient
    });

    heatmap.setMap(map);
};

document.head.appendChild(script);
      