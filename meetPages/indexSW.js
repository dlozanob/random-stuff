class Time {
    constructor() {
        this._hours = 0;
        this._min = 0;
        this._secs = 0;
        this._ms = 0;
    }

    get ms() {return this._ms;}
    get secs() {return this._secs;}
    get min() {return this._min;}
    get hours() {return this._hours;}

    set ms(t) {
        if(t >= 1000) {this.secs += Math.floor(t/1000);}
        this._ms = t%1000;
    }

    set secs(t) {
        if(t >= 60) {this.min += Math.floor(t/60);}
        this._secs = t%60;
    }

    set min(t) {
        if(t >= 60) {this.hours += Math.floor(t/60);}
        this._min = t%60;
    }

    set hours(t) {
        this._hours = t;
    }

    toDigit() {
        let digitAr = new Array();
        
        let msStr = (this._ms < 10) ? '00' : '';
        msStr += this._ms;
        digitAr.push(msStr);
        
        let secsStr = (this._secs < 10) ? '0' : '';
        secsStr += this._secs;
        digitAr.push(secsStr);

        let minStr = (this._min < 10) ? '0' : '';
        minStr += this._min;
        digitAr.push(minStr);

        let hStr = (this._hours < 10) ? '0' : '';
        hStr += this._hours;
        digitAr.push(hStr);

        return digitAr;
    }
}

let timeData = new Time();
var updater = null;

var dispTime = document.getElementById("dispTime");
var sBtn = document.getElementById("start");
var stBtn = document.getElementById("stop");
var rBtn = document.getElementById("reset");

sBtn.onclick = startCounter;
stBtn.onclick = stopCounter;
rBtn.onclick = resetCounter;

var audio = new Audio('ticTac3.mp3');
var ticCount = 0;


function updateCounter() {
    timeData.ms += 19;
    updateDisplay();

    ticCount += 19;
    if(ticCount >= 1000) {
        //audio.play();
        navigator.vibrate(200);
        ticCount = 0;
    }
}

function startCounter() {
    if(!updater) {updater = setInterval(updateCounter, 19);}
}

function stopCounter() {
    clearInterval(updater);
    updater = null;
}

function resetCounter() {
    stopCounter();
    timeData = new Time();
    updateDisplay();
}

function updateDisplay() {
    let timeAr = timeData.toDigit();
    dispTime.innerHTML = `${timeAr[3]}:${timeAr[2]}:${timeAr[1]}  <div id="ms">${timeAr[0]}</div>`;
}