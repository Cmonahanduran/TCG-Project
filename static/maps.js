



function initMap() {
    const map = new google.maps.Map(document.querySelector('#map'), {
      center: {
        lat: 37.601773,
        lng: -122.20287,
      },
      zoom: 11,
    });

    document.querySelector('#geocode-address').addEventListener('click', () => {
        const userAddress = prompt('Enter a location');
    
        const geocoder = new google.maps.Geocoder();
        geocoder.geocode({ address: userAddress }, (results, status) => {
          if (status === 'OK') {
            // Get the coordinates of the user's location
            const userLocation = results[0].geometry.location;
            
            // make fetch request to google places api
            // use for loop in second .then to create markers for each result
            // hopefully don't die
            // Create a marker
            var request = {
                location: userLocation,
                radius: '400',
                type: ['store']
            };
            service = new google.maps.places.PlacesService(map);
            service.nearbySearch(request, callback);
        
            function callback(results, status) {
                if (status == google.maps.places.PlacesServiceStatus.OK) {
                    for (var i = 0; i < results.length; i++){
                        new google.maps.Marker({
                            position: results[i],
                            map,
                        });
                    }
                }
            };

            new google.maps.Marker({
              position: userLocation,
              map,
            });

            map.setCenter(userLocation);
            map.setZoom(18);
          } else {
            alert(`Geocode was unsuccessful for the following reason: ${status}`);
          }
        });
      });


}

   