$( document ).ready(function() {
  $("#add-flux").click(function (event) {
    /*event.preventDefault();
    console.log('clicked');*/
    $("#add-flux").prop("disabled", true);
    setTimeout(function () {
      $("#add-flux").prop("disabled", false);
    }, 5000);

    /*$("#add-flux-form input[name='url']").val();
    $.ajax({
      url: '/add/',
      data: $("#add-flux-form").serialize(),
      method: 'POST',
      cache: false,
      success: function (data) {
        $("#add-flux").prop("disabled", false);
        if(data.status == 200) {
          console.log('saved: ' + data.data.saved + '\nskipped:' + data.data.skipped);
        } else if (data.status == 400) {
          alert('error ' + data.data);
        } else {
          alert('error')
        }
      },
      error: function (data) {
        alert('error');
      }
    });*/
  });
});
