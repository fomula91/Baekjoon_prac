const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
let input = [];
rl.on("line", (line) => {
    input.push(line);

}).on("close", () =>{
    let temp = [];
    let a = input[0].split(' ').map(el => parseInt(el));;
    let b = parseInt(input[1])
    temp[0] = parseInt(b / 60); 
    temp[1] = b % 60
    a[0] = a[0] + temp[0];
    a[1] = a[1] + temp[1];
    if(a[1] > 59){
        a[1] = a[1] - 60;
        a[0] = a[0] + 1;
        if(a[0] >= 24){
            a[0] = a[0] - 24;
        }

    }else if(a[0] > 23){
        a[0] = a[0] - 24;
    }
    console.log(a[0], a[1])
    process.exit()
})