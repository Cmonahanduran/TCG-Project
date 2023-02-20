

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
                radius: '1000',
                type: ['store', 'establishment','point_of_interest']
            };
            
        
            function callback(results2, status2) {
              console.log(results2)
                if (status2 == google.maps.places.PlacesServiceStatus.OK) {
                    for (var i = 0; i < results2.length; i++){
                        const marker = new google.maps.Marker({
                            position: results2[i].geometry.location,
                            map,
                        });
                          const infoWindow = new google.maps.InfoWindow({
                              content:`<p><b>${results2[i].name}</b></p>`,
                              disableAutoPan: true,
                          });

                        marker.addListener("click", () => {
                    
                            infoWindow.open(map, marker);
                        });

                    }
                }
            };
            service = new google.maps.places.PlacesService(map);
            service.nearbySearch(request, callback);




            map.setCenter(userLocation);
            map.setZoom(18);
          } else {
            alert(`Geocode was unsuccessful for the following reason: ${status}`);
          }
        });
      });


}