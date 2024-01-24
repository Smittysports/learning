/* 
POST: A request method supported by HTTP used by the World Wide Web. The POST request method
requests that a web server accept the data enclosed in the body of the request message,
most likely for storing it.

GET: A request method that retrieves information from the server. As part of a GET request,
some data can be passed within the URL's query string.

JSON: Here is an example JSON file
    {
        "name": "Brian",
        "ID": "1"
    }
The first quoted item is the key. The second quoted item, after the colon, is the value.


HTTP requires the use of CORS (Cross-Origin Resource Sharing).

CORS is a security feature implemented by web browsers that restricts web pages from making
requests to a different domain, protocol, or port than the one that served the web page.

The Fetch API provides a way to make HTTP requests from your web application. With Fetch,
you can specify the mode of the request using the mode option in the fetch() function.

The mode option can be set to one of four possible values: 'cors', 'no-cors', 'same-origin', 
or 'navigate'.
*/


function readProperty() {
    var serverIPAddress = document.getElementById("serverIPAddressTextInput").value
    var serverPort = document.getElementById("serverPortTextInput").value
    var deviceIPAddress = document.getElementById("deviceIPAddressTextInput").value
    var deviceID = document.getElementById("deviceIDTextInput").value
    var objectType = document.getElementById("objectTypeTextInput").value
    var objectID = document.getElementById("objectIDTextInput").value
    var propertyName = document.getElementById("propertyNameInput").value

    let command = {
        "deviceIPAddress": deviceIPAddress,
        "deviceID": deviceID,
        "objectType": objectType,
        "objectID": objectID,
        "propertyName": propertyName,
        "propertyDataType": 'none',
        "propertyValue": '0'
    }

    post(serverIPAddress, serverPort, command)
}

function writeProperty() {
    var serverIPAddress = document.getElementById("serverIPAddressTextInput").value
    var serverPort = document.getElementById("serverPortTextInput").value
    var deviceIPAddress = document.getElementById("deviceIPAddressTextInput").value
    var deviceID = document.getElementById("deviceIDTextInput").value
    var objectType = document.getElementById("objectTypeTextInput").value
    var objectID = document.getElementById("objectIDTextInput").value
    var propertyName = document.getElementById("propertyNameInput").value
    var propertyDataType = document.getElementById("propertyDataTypeInput").value
    var propertyValue = document.getElementById("propertyValueInput").value

    let command = {
        "deviceIPAddress": deviceIPAddress,
        "deviceID": deviceID,
        "objectType": objectType,
        "objectID": objectID,
        "propertyName": propertyName,
        "propertyDataType": propertyDataType,
        "propertyValue": propertyValue
    }

    post(serverIPAddress, serverPort, command)
}

/* This method works as a POST.
 *
 * It will trigger the do_POST in the server.
 * 
 * TODO: 1) Add the ability to pass in what I want to post
 *       2) Add the ability to save IP data in a cookie so that other aspects of this
 *          webpage can use that information
*/
async function post(serverIPAddress, serverPort, command) {    
    addressOfServer = 'http://' + serverIPAddress + ':' + serverPort
    let response = await fetch(addressOfServer, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(command)
    });
    
    let result = await response.json();
    handleReponse(result)
}

function handleReponse(response) {
    console.log(response)

    var dictionary = JSON.parse(response);
    for (const [key, value] of Object.entries(dictionary)) {
        console.log(key, ":", value);
    }
}

/* This method works as a GET.
 *
 * It will trigger the do_GET in the server.
*/
async function get() {
    fetch('http://192.168.1.101:8000')
        .then((response) => {
            console.log("resolved", response);
            return response.json();
        })
        .then((data) => {
            console.log(data);
        })
        .catch((err) => {
            console.log("error retrieving data", err);
        }
    );
}

