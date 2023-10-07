$(document).ready(function () {
  const myHeader = $('#red_header');
  myHeader.click(() => {
    $('header').css('color', '#FF0000');
  });
});
