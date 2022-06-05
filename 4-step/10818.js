let readline = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const [a, b] = readline.slice(0, -1);
const getArr = b.split(" ");
let arr = [];
getArr.map((value) => {
  arr.push(parseInt(value));
});
arr.sort((a, b) => a - b);
console.log(arr.slice(0, 1).toString(), arr.slice(-1).toString());
