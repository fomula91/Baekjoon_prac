const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    let num = []
    num=map(line)
}).on("close", () => {
    process.exit()
})