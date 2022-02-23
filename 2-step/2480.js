const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
rl.on("line", (line) => {
    let input = [];
    input = line.split(' ').map(el => parseInt(el))
    if(input[0] === input[1] === input[2]){
        let result = (10000 + input[0]) * 1000
        console.log(result)
    }else if(input[0] === input[1] || input[0] === input[2] || input[1]===input[2] || input[0] === input[2]){
        console.log("2수 같음 ")
    }else if(input[0] !== input[1] !== input[2]){
        console.log("모두 다름")
    }else{
        console.log("몰?루")
    }
    rl.close()
}).on("close", () => {
    process.exit()
})