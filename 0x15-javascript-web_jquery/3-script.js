$(document).ready(function () {
  const myHeaderId = $('#red_header');
  const myHeader = $('header');
  myHeaderId.click(() => {
    myHeader.addClass('red');
  });
});
