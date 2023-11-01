$(document).ready(function () {
  $('#btn_translate').click(translateHello);
  $('#language_code').on('keyup', function (event) {
    if (event.key === 'Enter') {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
