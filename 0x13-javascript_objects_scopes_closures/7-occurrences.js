#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  list.forEach(element => {
    if (element === searchElement) {
      occur++;
    }
  });
  return (occur);
};
