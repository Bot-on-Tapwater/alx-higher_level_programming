#!/usr/bin/node

let argCnt = 0;

exports.logMe = function (item) {
  console.log(`${argCnt}: ${item}`);
  argCnt++;
};
