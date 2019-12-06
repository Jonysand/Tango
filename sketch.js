let transMatrix;
let tempKey = '1';
let preKey = '1';
let tempState = 31; // inital state as the first note of the song
let note_list = [54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 93, 94, 96];


function preload() {
    transMatrix = loadTable('data/transMatrix.csv', 'csv');
}

function setup() {
    osc = new p5.Oscillator('sine');
    osc.start();
}

function draw() {
    
}

function keyPressed() {
    if('1'<=key && key<='9'){
        tempKey = key;
        let freq = midiToFreq(note_list[tempState]);
        osc.freq(freq);
        tempState = findNextState(tempState, transMatrix);
        console.log(tempState);
    }
}


//--------------------------------
function findNextState(tempState, transMatrix){
    let i = 0;
    let upperBound = transMatrix.getRowCount();
    let randNum = random();
    let thisRow = transMatrix.getRow(tempState);
    
    if(tempKey==preKey){
        return tempState;
    }else if(tempKey > preKey){
        if(tempState<transMatrix.getRowCount()-1){
            i = tempState+1;
        }else{
            return tempState;
        }
    }else if(tempKey < preKey){
        if(tempState>1){
            upperBound = tempState;
        }else{
            return tempState;
        }
    }
    
    for (; i<upperBound ;i++){
        if (thisRow.arr[i]>=randNum) break;
    }
    
    preKey = tempKey;
    return i;
}
