const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on('line', (line) => {
    let number = []
    number = line.split(' ');
    a = parseInt(number[0]);
    b = parseInt(number[1]);
    if(a > b){
        console.log('>')
    }
    else if(a < b){
        console.log('<')
    }
    else if(a == b){
        console.log('==')
    }
    rl.close()
}).on('close', () => {
    process.exit()
})