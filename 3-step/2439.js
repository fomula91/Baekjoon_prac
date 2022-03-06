const readline = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let CreateNum = parseInt(readline), star = '*', tempStar = '', space = ' ', result = '';

for(let i = CreateNum; 0 < i; i--){
    for(let j = 1; j < i; j++){
        tempStar += space;
    }
    for(let k = 0; k <= CreateNum - i; k++){
        tempStar += star;    
    }
    result += tempStar + '\n';
    tempStar = '';
}
console.log(result);