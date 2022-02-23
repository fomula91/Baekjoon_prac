const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
let input = [];
rl.on("line", (line) => {
    input.push(line)
})
rl.on("close", () =>{
    let a = parseInt(input[0]);
    let b = parseInt(input[1]);
    if(a > 0){
        if(b > 0){
            console.log(1)
        }
        else if(b < 0){
            console.log(4)
        }
    }
    else if(a < 0){
        if( b < 0){
            console.log(3)
        }
        else if(b > 0){
            console.log(2)
        }
    }
    process.exit();
})