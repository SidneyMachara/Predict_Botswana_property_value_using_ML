var BASE_URL = "http://127.0.0.1:5000";

// executed when page loads to get the loactions and populates the html's select
function onPageLoad() {
  var url = BASE_URL + "/get_location_names";

  $.get(url,function(response) {
      var locations = response.locations;

      $('#locations').empty();

      for(var i in locations) {
          var location = new Option(locations[i]);
          $('#locations').append(location);
      }

  });
}

$("#prediction_form").submit(function(event) {
     // prevent reload
     event.preventDefault();
     var $form = $( this );

     var url = BASE_URL + "/predict_property_price";

     // get values
     var plot_size = $("#plot_size").val();
     var num_bathrooms = $("#num_bathrooms").val();
     var num_bedrooms = $("#num_bedrooms").val();
     var locations = $("#locations").val();

     // cross your fingers and pray it works
     $.post(url, {
         location: locations,
         plot_size: plot_size,
         num_bathrooms: num_bathrooms,
         num_bedrooms: num_bedrooms
     },function(response) {
         $("#price_box").html("<h1 class='text-center' style='color:#b2ebf2'>" + formatFloatToPulas(response.price_estimate) + "</h1>");
     });
   });

// make price human readable
function formatFloatToPulas(price) {
  return new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'BWP',
}).format(price)

}

// run on page start
window.onload = onPageLoad;
