let map;

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyApBGLyOG3tTnJsCjj1_vDeimFp72_xF0Y&libraries=visualization&callback=initMap';
script.async = true;

// Attach your callback function to the `window` object
window.initMap = async function() {
    const { Map } = await google.maps.importLibrary("maps");

    function getRandomLatLng() {
      const minLat = 24.396308; 
      const maxLat = 49.384358;
      const minLng = -125.000000; 
      const maxLng = -66.934570;
      
      const lat = Math.random() * (maxLat - minLat) + minLat;
      const lng = Math.random() * (maxLng - minLng) + minLng;
    
      return { lat, lng };
    }
    
    function getSmoothWeight() {
      return Math.random() * 100;
    }
    
    const points = [];
    for (let i = 0; i < 1000; i++) {
      const { lat, lng } = getRandomLatLng();
      const weight = getSmoothWeight();
      const point = {
        location: new google.maps.LatLng(lat, lng),
        weight: weight.toFixed(6)
      };
      points.push(point);
    }

    // bigger weight = more red
    var alabama = new google.maps.LatLng(32.806671, -86.791130);
  
    map = new Map(document.getElementById("map"), {
      center: alabama,
      zoom: 8
    });

    const gradient = [
        "rgba(0, 255, 0, 0.15)",
        "rgba(255, 165, 0, 0.35)",
        "rgba(255, 0, 0, 1)",
        "rgba(139, 0, 0, 1)"
    ];

    var heatmap = new google.maps.visualization.HeatmapLayer({
      data: points,
      radius: 1,
      maxIntensity: 100,
      dissipating: false,
      gradient: gradient
    });

    heatmap.setMap(map);
};

// Append the 'script' element to 'head'
document.head.appendChild(script);
      