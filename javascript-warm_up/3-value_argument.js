#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
/* #!/usr/bin/node
if (process.argv[2]) {
  console.log('process.argv[2]');
} else {
  console.log('No argument');
}
*/
