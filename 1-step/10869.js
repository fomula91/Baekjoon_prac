const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    let input = [];
    input = line.split(' ').map(el => parseInt(el));
    let a = input[0];
    let b = input[1];
    console.log(a+b);
    console.log(a-b);
    console.log(a*b);
    console.log(parseInt(a/b));
    console.log(a%b);
    rl.close();
})
rl.on("close", () => {
    process.exit();
})