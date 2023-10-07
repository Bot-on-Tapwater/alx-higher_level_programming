$(document).ready(function () {
  const myList = $('UL.my_list');
  const addItem = $('DIV#add_item');

  addItem.click(() => {
    const listItem = $('<li>Item</li>');
    myList.append(listItem);
  });
});
