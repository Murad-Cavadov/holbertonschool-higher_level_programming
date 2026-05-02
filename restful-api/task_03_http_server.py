#!/usr/bin/python3
"""
Python-un http.server modulu ilə qurulmuş sadə API serveri.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP GET sorğularını idarə edən xüsusi handler sinfi.
    """

    def do_GET(self):
        """GET sorğuları üçün marşrutlaşdırma (routing) məntiqi."""
        
        # 1. Kök endpoint: /
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Data endpoint: /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 3. Status endpoint: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Info endpoint: /info
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # 5. Xəta: Tapılmayan endpointlər (404)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Serveri 8000 portunda başladır."""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server 8000 portunda işləyir...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
