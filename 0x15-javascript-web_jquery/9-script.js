const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.ajax({
  url,
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    $(document).ready(function () {
      const helloDiv = $('DIV#hello');
      helloDiv.text(data.hello);
    }
    );
  },
  error: function (xhr, status, error) {
    console.error('Ajax error:', error);
  }
});
