// Search script
function searchSuccess(data, textStatus, jqXHR) {
  console.log(data['result'].length)
  if (data['result'].length > 0) {
    $('#search-results').html( "<ul>" + "<a href=\"" + data["result"][0]["url"] + "\">" + data["result"][0]["title"] +  "</a>" + "</ul>");
  }
}

//Profile dropdown show/hide
$(document).ready(function(){
  $("#account").click(function(){
    $("#dropdown-container").toggle();
    $('#search-results').hide();
    $('#search-show').hide();
    $('#search-button').show();
  });
  $(window).click(function() {
    $('#dropdown-container').hide();
  });
  $(".navbar-account").click(function(event){
    event.stopPropagation();
  });
  $('#dropdown-container').click(function(event){
    event.stopPropagation();
  });
  $('#click-hide').click(function(){
    $('#search-show').hide();
    $('#search-button').show();
    $('#search-results').hide();
  });
  $('#search-button').click(function(){
    $('#search-show').animate({width:'toggle'}, 450, function(){
      $(this).show();
    });
    $('#search-button').hide();
    $('#search-results').show();
    $("#dropdown-container").hide(150);
  });
  $('#search-hide').click(function(){
    $('#search-show').hide();
    $('#search-button').show();
    $('#search-results').hide();
  });
});
