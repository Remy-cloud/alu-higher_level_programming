#!/usr/bin/node
const args1 = parseInt(process.argv[2]);
const args2 = parseInt(process.argv[3]);

function add(a, b){
    return a + b;
}
console.log(add(args1, args2));
