const readline = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .slice(0, -1);

let myNum = {};
const index = 10;
for (i = 0; i < index; i++) {
  myNum[i] = 0;
}
const inputArr = readline
  .map((value) => parseInt(value))
  .reduce((prev, cur) => prev * cur)
  .toString()
  .split("");
inputArr.map((value) => (myNum[value] = myNum[value] + 1));
for (i = 0; i < index; i++) {
  console.log(myNum[i]);
}
