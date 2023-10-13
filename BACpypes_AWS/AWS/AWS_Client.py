#!/usr/bin/env python3
"""An example HTTP server with GET and POST endpoints."""
from bacpypes.consolelogging import ArgumentParser
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import AWS_ReadProperty
import json
import time

server_ip_address = "192.168.1.101"
device_ip_address = "0.0.0.0"
device_ID = 0

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

        print("do_POST")
        
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        # The data is passed in via json. It is stored in python in a dictionary
        for key in message:
            if key == 'deviceIPAddress':
                device_ip_address = message[key]
            elif key == 'deviceID':
                device_ID = message[key]
        
        print("device_ip_address = ", device_ip_address)
        print("device_ID = ", device_ID)
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
    server_address = (server_ip_address, 8000)
    httpd = HTTPServer(server_address, _RequestHandler)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)

    parser.add_argument('server_ip_address', type=str,
        help='server ip address',
    )

    args = parser.parse_args()
    run_server()