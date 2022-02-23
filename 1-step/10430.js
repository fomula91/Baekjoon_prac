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
    let c = input[2];

    
    console.log((a+b)%c);
    console.log(((a%c) + (b%c))%c);
    console.log((a*b)%c);
    console.log(((a%c)*(b%c))%c);
    rl.close();

})
rl.on("close", () => {
    process.exit();
})