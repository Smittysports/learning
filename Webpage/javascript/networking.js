
function connect() {
  console.log("Connect")

  fetch('http://192.168.1.11:47808') 
    .then(function(response) { 
        console.log("Got it");
    }, function(e) {
        console.log("Error");
    })
}
  
