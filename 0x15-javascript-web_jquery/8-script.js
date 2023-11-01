$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movieList = data.results;
    $.each(movieList, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
