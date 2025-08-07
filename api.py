from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Welcome to the root endpoint!"}
            self.wfile.write(json.dumps(response).encode())
        elif self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Hello, world!"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == "/echo":
            contant=int(self.headers.get('Content-Length',0))
            body=self.rfile.read(contant)
            data=json.loads(body)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"you_sent": data}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404, "Not Found")

def run(server_class=HTTPServer, handler_class=SimpleAPI, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
