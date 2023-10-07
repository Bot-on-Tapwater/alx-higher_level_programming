$(document).ready(function () {
  const myHeader = $('header');
  const updateHeader = $('DIV#update_header');

  updateHeader.click(() => {
    myHeader.text('New Header!!!');
  });
});
