const readline = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .slice(0, -1);

const number = readline.map((value) => parseInt(value) % 42);
const set = new Set(number);
const result = [...set];
console.log(result.length);
