let tiles = document.querySelector(".row");

var initPos = 3;
var intTime = 40;
var secondsToLast = 6;
var tmr;

var shift = -90;
var damp = -0.055;
var period = 1/12;
var factor = 15;
var time = 0;

tiles.style.left = "1500px";
tmr = setInterval(bounce, intTime);

function bounce() {
    let translation = factor*Math.exp(damp*(time + shift))*Math.sin(period*Math.PI*(time + shift));
    
    tiles.style.left = `${-translation}px`;
    time += 1;

    if(time >= secondsToLast*1000/intTime) {
        tiles.style.left = "0";
        clearInterval(tmr);
    }
};
