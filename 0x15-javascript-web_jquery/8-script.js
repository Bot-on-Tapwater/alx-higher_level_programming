const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
  url,
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    $(document).ready(function () {
      const movieList = $('UL#list_movies');
      data['results'].forEach((value, index)=>{
        let listItem = $("<li>" + value["title"] + "</li>");
        movieList.append(listItem);
      })
    }
    );
  },
  error: function (xhr, status, error) {
    console.error('Ajax error:', error);
  }
});
