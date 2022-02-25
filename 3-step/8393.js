const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    let getNum = parseInt(line);
    let num = 0;
    for(let i = 0; i <= getNum; i++){
        num = num+i;
        
    }
    console.log(num)
    rl.close()
}).on("close", () =>{
    process.exit()
})