let tiles = document.querySelector(".row");

var initPos = 3;
var tmr;

var shift = -93;
var damp = -0.04;
var period = 1/6;
var factor = 30;
var time = 0;

tiles.style.left = "1500px";
tmr = setInterval(displace, 60);

function displace() {
    let translation = factor*Math.exp(damp*(time + shift))*Math.sin(period*Math.PI*(time + shift));
    console.log(`Result is: ${translation}`);
    tiles.style.left = `${-translation}px`; 
    time += 1;
};