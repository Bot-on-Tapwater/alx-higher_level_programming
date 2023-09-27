#!/usr/bin/node

/* path to file parsed as CMD args */
// const filePath = process.argv[3];
const urlReq = process.argv[2];

const request = require('request');
const usersDict = {};

request(urlReq, (error, response, body) => {
  if (error) throw error;
  const content = JSON.parse(body);
  content.forEach((value) => {
    const user = value.userId;
    const task = value.completed;

    if (task === true) {
      // console.log(user, task);
      usersDict[user] = 0;
    }
  });

  content.forEach((value) => {
    const user = value.userId;
    const task = value.completed;

    if (task === true) {
      // console.log(user, task);
      usersDict[user]++;
    }
  });
  console.log(usersDict);
});
