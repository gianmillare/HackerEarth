// Basics of Input/Output
// https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/tutorial/

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
   main(stdin_input);
});

function main(input) {
    var data = input.split('\n');
    process.stdout.write((parseInt(data[0]) * 2).toString() + "\n");
    process.stdout.write(data[1]); 
}