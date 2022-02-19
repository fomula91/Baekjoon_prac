const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
let input2 = [];
let result = [];

rl.on('line', function (line) {
  input.push(line)
})
  .on('close', function () {
  a = parseInt(input[0]);
  b = parseInt(input[1]);
  
  input2 = input[1].split('').map(el => parseInt(el))
  for(let i in input2){
    temp = input2[i] * a
    result.push(temp)
  }

  console.log(result[2])
  console.log(result[1])
  console.log(result[0])
  console.log(a*b)
  
  process.exit();
});