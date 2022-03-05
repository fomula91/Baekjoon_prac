const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
    let arr = [];
rl.on("line", (line) => {
    arr.push(line.split(' '));
}).on("close", () =>{
    for(let i = 1; i <= parseInt(arr[0]); i++){
        console.log(`Case #${i}: ${parseInt(arr[i][0])} + ${parseInt(arr[i][1])} = ${parseInt(arr[i][0])+parseInt(arr[i][1])}`)
    }
    rl.close();
    process.exit();
})