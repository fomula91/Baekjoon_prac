const readline = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

let a = 0;
let b = 0;
const inputNum = readline.slice(0, -1);
const typeNum = inputNum.map((value) => {
  return parseInt(value);
});
for (let i = 0; i < typeNum.length; i++) {
  if (a < typeNum[i]) {
    a = typeNum[i];
    b = i + 1;
  }
}
console.log(a);
console.log(b);
