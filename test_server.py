from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class TestServerHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        print(f"Received HEAD request from: {self.client_address[0]}")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_POST(self):
        content_type, _ = self.headers.get('Content-Type', '').split(';')
        if content_type == 'application/x-www-form-urlencoded':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = urllib.parse.parse_qs(post_data)
            print(f"Received data: {data}")

            # You can process the received data here or store it in a database, etc.

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Data received successfully!")
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Invalid Content-Type. Expected 'application/x-www-form-urlencoded'.")

def run(server_class=HTTPServer, handler_class=TestServerHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
