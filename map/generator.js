const fs = require('fs');

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
for (let i = 2023; i <= 2050; i++) {
    points.push([])
    
    for (let j = 0; j < 10000; j++) {
        const { lat, lng } = getRandomLatLng();
        const weight = getSmoothWeight();
        const point = {
            location: { lat, lng },
            weight: weight.toFixed(6)
        };

        points[i - 2023].push(point);
    }
}

const jsonData = JSON.stringify(points, null, 2);

fs.writeFile('points.json', jsonData, (err) => {
  if (err) {
    console.error('Error w  riting to file:', err);
  } else {
    console.log('Points written to points.json');
  }
});