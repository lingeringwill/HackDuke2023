let map;

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyApBGLyOG3tTnJsCjj1_vDeimFp72_xF0Y&libraries=visualization&callback=initMap';
script.async = true;

// Attach your callback function to the `window` object
window.initMap = async function() {
    const { Map } = await google.maps.importLibrary("maps");

    var heatMapData = [
      {location: new google.maps.LatLng(32.806671, -86.791130)}, // alabama
      {location: new google.maps.LatLng(61.370716, -152.404419)}, // alaska
      {location: new google.maps.LatLng(33.729759, -111.431221)}, // arizona
      {location: new google.maps.LatLng(34.969704, -92.373123)}, // arkansas
      {location: new google.maps.LatLng(36.116203, -119.681564)}, // california
      {location: new google.maps.LatLng(39.059811, -105.311104)}, // colorado
      {location: new google.maps.LatLng(41.597782, -72.755371)}, // conneticut
      {location: new google.maps.LatLng(39.318523, -75.507141)}, // delaware 
      {location: new google.maps.LatLng(38.897438, -77.026817)}, // district of columbia
      {location: new google.maps.LatLng(27.766279, -81.686783)}, // florida
      {location: new google.maps.LatLng(33.040619, -83.643074)}, // georgia
      {location: new google.maps.LatLng(21.094318, -157.498337)} // hawaii
    ]

    var alabama = new google.maps.LatLng(32.806671, -86.791130);
  
    map = new Map(document.getElementById("map"), {
      center: alabama,
      zoom: 8
    });
  
    var heatmap = new google.maps.visualization.HeatmapLayer({
      data: heatMapData
    });

    heatmap.set("radius", 5);
    heatmap.set("dissipating", false);
  
    heatmap.setMap(map);
};

// Append the 'script' element to 'head'
document.head.appendChild(script);
      