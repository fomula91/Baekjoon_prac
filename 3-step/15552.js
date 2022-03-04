const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
    let arr = [];
    let arr2 = [];
    let answer = '';
rl.on("line", (line) => {
    arr.push(line.split(' '));
}).on("close", () =>{
    for(let i = 1; i <= parseInt(arr[0]); i++){
        arr2.push(parseInt(arr[i][0])+parseInt(arr[i][1]));
        answer += arr2[i-1]+'\n';
    }
    console.log(answer);
    rl.close();
    process.exit();
})