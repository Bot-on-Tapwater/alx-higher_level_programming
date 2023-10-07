$(document).ready(function () {
  const myHeaderId = $('#toggle_header');
  const myHeader = $('header');
  myHeaderId.click(() => {
    // myHeader.addClass('red')
    if (myHeader.hasClass('red')) {
      myHeader.removeClass('red').addClass('green');
    } else {
      myHeader.removeClass('green').addClass('red');
    }
  });
});
