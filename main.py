import http.server
import socketserver
from http import HTTPStatus

version = '0.0.1'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(str.encode('Simple HTTP server @ version %s' % version))


httpd = socketserver.TCPServer(('', 8000), Handler)
print("HTTP server started")
httpd.serve_forever()
