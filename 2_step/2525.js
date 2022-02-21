const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    console.log(parseInt(parseInt(line)/60))
    console.log(parseInt(line)%60)
    rl.close();
}).on("close", () =>{
    process.exit()
})