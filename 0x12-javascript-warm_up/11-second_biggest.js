#!/usr/bin/node
let lgst = 0;
let sndLgst = 0;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.forEach(element => {
    if (element > lgst) {
      lgst = element;
    }
  });
  process.argv.forEach(element => {
    if (element > sndLgst && element < lgst) {
      sndLgst = element;
    }
  });
  console.log(sndLgst);
}
