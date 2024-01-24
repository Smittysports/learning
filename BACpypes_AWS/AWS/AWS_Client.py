#!/usr/bin/env python3
"""An example HTTP server with GET and POST endpoints."""
from bacpypes.consolelogging import ArgumentParser
from bacpypes.local.device import LocalDeviceObject
from bacpypes.core import run, deferred, stop
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from AWS_ReadProperty import ReadPropertyApplication
import json
import time

server_ip_address = "192.168.1.101"
device_ip_address = "0.0.0.0"
device_ID = 0
objectType = "analogInput"
objectID = 1
propertyName = "objectName"
propertyDataType = 'none'
propertyValue = "0"
this_device = 'none'
this_application = 'none'

class _RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        print("do_GET")
        self._set_headers()
        response = json.dumps({'hello': 'world', 'received': 'ok'})
        response = bytes(response, 'utf-8')
        self.wfile.write(response)

    def do_POST(self):
        global device_ip_address
        global device_ID
        global objectType
        global objectID
        global propertyName
        global this_device
        global this_application

        print("do_POST")
        
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        # The data is passed in via json. It is stored in python in a dictionary
        for key in message:
            if key == 'deviceIPAddress':
                device_ip_address = message[key]
            elif key == 'deviceID':
                device_ID = message[key]
            elif key == 'objectType':
                objectType = message[key]
            elif key == 'objectID':
                objectID = message[key]
            elif key == 'propertyName':
                propertyName = message[key]
            elif key == 'propertyDataType':
                propertyDataType = message[key]
            elif key == 'propertyValue':
                propertyValue = message[key]
        
        print("device_ip_address = ", device_ip_address)
        print("device_ID = ", device_ID)
        print("objectType = ", objectType)
        print("objectID = ", objectID)
        print("propertyName = ", propertyName)

        #{'objectname': 'AWS_BACpypesClient', 'address': '192.168.1.101/24', 'objectidentifier': '598', 'maxapdulengthaccepted': '1024', 'segmentationsupported': 'segmentedBoth', 'vendoridentifier': '10'}
        server_ip_address_full = server_ip_address + '/24'
        args_str = {'objectname': 'AWSClient', 'address': server_ip_address_full, 'objectIdentifier': '598', 'maxApduLengthAccepted': '1024', 'segmentationSupported': 'segmentedBoth', 'vendorIdentifier': '10'}
        # If the data type is none, it is for reading
        if (propertyDataType == 'none'):
            if (this_device == 'none'):
                this_device = LocalDeviceObject(ini=args_str)
                this_application = ReadPropertyApplication(this_device, server_ip_address_full)
            # TODO: This part does not work. I need ti create a single Application for Read/write and then communicate with it
            deferred(this_application.read_property_value, device_ID, device_ip_address, objectType, objectID, propertyName)

        else:
            print("propertyDataType = ", propertyDataType)
            print("propertyValue = ", propertyValue)

        # TODO: Call into AWS_ReadProperty and read from the device
        self._set_headers()
        
        json_string = json.dumps(message)
        self.wfile.write(json.dumps(json_string).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()


def run_server():
    server_address = (server_ip_address, server_port)
    httpd = HTTPServer(server_address, _RequestHandler)
    print('serving at %s:%d' % (server_address, server_port))
    httpd.serve_forever()


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)

    parser.add_argument('server_ip_address', type=str,
        help='server ip address',
    )

    parser.add_argument('server_port', type=int,
        help='server port',
    )
    
    args = parser.parse_args()

    server_ip_address = args.server_ip_address
    server_port = args.server_port

    run_server()