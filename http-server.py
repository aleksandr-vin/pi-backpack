#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import subprocess

PORT_NUMBER = 80

class myHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/plain')
    self.end_headers()
    out = subprocess.check_output(["/home/pi/stats"])
    self.wfile.write(out)
    return

try:
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print('Started httpserver on port ' , PORT_NUMBER)
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()
