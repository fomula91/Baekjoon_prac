const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let data = parseInt(input);
let answer = '';
for(let i = data; 0 < i; i--){
    answer += `${i}\n`;
}
console.log(answer);
