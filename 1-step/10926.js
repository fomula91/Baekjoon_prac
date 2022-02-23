// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// })

// rl.on("line", (line) => {
    
//     console.log(`${line}??!`)
//     rl.close();
// })

// rl.on("close", () => {
//     process.exit();
// })

const fs = require('fs');

const input = fs.readFileSync("/dev/stdin").toString().trim();

console.log(`${input}??!`);