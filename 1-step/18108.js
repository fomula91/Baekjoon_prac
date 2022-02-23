const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    let input = parseInt(line);

    console.log(input - 543);
    rl.close();
}).on("close", () =>{
    process.exit();
})