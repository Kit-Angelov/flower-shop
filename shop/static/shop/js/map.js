function initMap() {
    var uluru = {lat: 51.67083185, lng: 39.18866158};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 1,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
  }