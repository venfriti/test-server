from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class TestServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_type, _ = cgi.parse_header(self.headers['Content-Type'])
        if content_type == 'application/x-www-form-urlencoded':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            print(f"Received data: {post_data}")

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
