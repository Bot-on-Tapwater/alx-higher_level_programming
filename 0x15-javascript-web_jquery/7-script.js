const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.ajax({
  url,
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    $(document).ready(function () {
      const charDiv = $('DIV#character');
      charDiv.text(data.name);
    }
    );
  },
  error: function (xhr, status, error) {
    console.error('Ajax error:', error);
  }
});
