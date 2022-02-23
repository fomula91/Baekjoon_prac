const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    let input = [];
    input = line.split(' ').map(el => parseInt(el))
    let a = input[0]
    let b = input[1]
    if(a >0){
        if(b>=45){
            b = b - 45
        }
        else if(b<45){
            a = a - 1
            b = (b-45) + 60
        }
    }
    else if(a <= 0){
        if(b >= 45){
            b = b - 45
        }
        else if(b < 45){
            a = 23
            b = (b-45) + 60
    }}
    console.log(`${a} ${b}`)
    rl.close();
}).on("close", ()=>{
    process.exit()
})