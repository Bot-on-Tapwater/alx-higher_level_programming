#!/usr/bin/node
let lgst = 0;
let sndLgst = 0;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.forEach(element => {
    if (parseInt(element) > lgst) {
      lgst = parseInt(element);
    }
  });
  /* console.log(`Largest elem: ${lgst}`); */
  process.argv.forEach(element => {
    if (parseInt(element) > sndLgst && parseInt(element) < lgst) {
      sndLgst = parseInt(element);
    }
  });
  console.log(sndLgst);
}
