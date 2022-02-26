let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let data = parseInt(input);
let answer = '';
for(let i = 1; i <= data; i++){
    answer += i+"\n";
}
console.log(answer);