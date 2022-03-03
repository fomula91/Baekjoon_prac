const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
rl.on("line", (line) => {
    let input = [];
    input = line.split(' ').map(el => parseInt(el))
    const a = input[0];
    const b = input[1];
    const c = input[2];
    let result;
    
    if(a == b && a != c){
        result = 1000 + (a * 100);
        console.log(result);
    }
    else if(a == c && b != c){
        result = 1000 + ( a * 100);
        console.log(result);
    }
    else if(b == c && a != c){
        result = 1000 + (b * 100);
        console.log(result);
    }
    else if(a != b && a != c && b != c){
        if(a > b){
            if(a > c){
                result = a * 100;
                console.log(result);
            }
            else{
                result = c * 100;
                console.log(result);
            }
        }
        else if(a < b){
            if(b > c){
                result = b * 100;
                console.log(result);
            }
            else{
                result = c * 100;
                console.log(result);
            }
        }
        
    }
    else{
        result = 10000 + (a * 1000);
        console.log(result);
    }
    
    rl.close()
}).on("close", () => {
    process.exit()
})