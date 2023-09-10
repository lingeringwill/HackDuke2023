let map;
let index = 0;
let points = [];
let current;

var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyApBGLyOG3tTnJsCjj1_vDeimFp72_xF0Y&libraries=visualization&callback=initMap';
script.async = true;

function createLeft(map) {
  const controlButton = document.createElement('button');

  controlButton.style.backgroundColor = '#fff';
  controlButton.style.border = '2px solid #fff';
  controlButton.style.borderRadius = '3px';
  controlButton.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
  controlButton.style.color = 'rgb(25,25,25)';
  controlButton.style.cursor = 'pointer';
  controlButton.style.fontFamily = 'Roboto,Arial,sans-serif';
  controlButton.style.fontSize = '16px';
  controlButton.style.lineHeight = '38px';
  controlButton.style.margin = '8px 30px 22px';
  controlButton.style.padding = '0 5px';
  controlButton.style.textAlign = 'center';

  controlButton.textContent = 'Decrement Year';
  controlButton.title = 'Click to decrement year';
  controlButton.type = 'button';  

  controlButton.addEventListener('click', () => {
      if (index != 0) {
        index--;
        current.clear();

        for (let i = 0; i < points[index].length; i++) {
          current.push(points[index][i]);
        }

        console.log(current);
      }
  });

  return controlButton;
}

function createRight(map) {
  const controlButton = document.createElement('button');

  controlButton.style.backgroundColor = '#fff';
  controlButton.style.border = '2px solid #fff';
  controlButton.style.borderRadius = '3px';
  controlButton.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
  controlButton.style.color = 'rgb(25,25,25)';
  controlButton.style.cursor = 'pointer ';
  controlButton.style.fontFamily = 'Roboto,Arial,sans-serif';
  controlButton.style.fontSize = '16px';
  controlButton.style.lineHeight = '38px';
  controlButton.style.margin = '8px 0 22px';
  controlButton.style.padding = '0 5px';
  controlButton.style.textAlign = 'center';

  controlButton.textContent = 'Increment Year';
  controlButton.title = 'Click to increment year';
  controlButton.type = 'button';  

  controlButton.addEventListener('click', () => {
      if (index != 27) {
        index++;
        current.clear();

        for (let i = 0; i < points[index].length; i++) {
          current.push(points[index][i]);
        }

        console.log(current);
      }
  });

  return controlButton;
}


window.initMap = async function() {
    const { Map } = await google.maps.importLibrary("maps");

    await fetch("points.json")
      .then((response) => response.json())
      .then((json) => loadPoints(json))

    async function loadPoints(json) {
        let top =    49.384297
        let right = -66.888932
        let bottom = 24.546337
        let left = -124.731077
      
        for (let i = 2023; i <= 2050; i++) {
            points.push(new Array());

            for (let j = 0; j < json[i].length; j++) {           
                let long = top - j * 1 // !
                for (let k = 0; k < json[i][j].length; k++) {
                    let lat = k * 1 + left; // !
                    let obj = json[i][j][k];
                    points[i - 2023].push({location: new google.maps.LatLng(lat, long), weight: obj});
                }
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

    current = new google.maps.MVCArray([]);
    
    for (let i = 0; i < points[index].length; i++) {
      current.push(points[index][i]);
    }

    let heatmap = new google.maps.visualization.HeatmapLayer({
      data: current,
      radius: 0.3,
      maxIntensity: 100,
      dissipating: false,
      gradient: gradient
    });

    heatmap.setMap(map);

    const controlDiv = document.createElement('div');
    const leftControl = createLeft(map);
    const rightControl = createRight(map);
    controlDiv.appendChild(leftControl);
    controlDiv.appendChild(rightControl);

    map.controls[google.maps.ControlPosition.TOP_CENTER].push(controlDiv);
};


document.head.appendChild(script);
      