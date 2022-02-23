const readline = require("readline");
 
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
 
let input = [];
 
rl.on("line", (line) => {
    input = line.split(' ').map(el => parseInt(el));
    let a = input[0];
    let b = input[1];

    console.log(a+b)
    rl.close();
});
 
rl.on('close', () => {
    
    process.exit();
})