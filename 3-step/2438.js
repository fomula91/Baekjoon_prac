const readline = require('fs').readFileSync('/dev/stdin').toString().split('\n')

let CreateNum = parseInt(readline);
let star = '*';
let tempStar = '';
let result;

for(let i = 0; i < CreateNum; i++){
    tempStar += star;
    result += tempStar + '\n';
    console.log(tempStar);
}