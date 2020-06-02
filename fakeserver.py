from BaseHTTPServer import BaseHTTRequestHandler,HTTPServer

class fakewebserver(BaseHTTRequestHandler):
    def send_response(self, code, message=None):
        self.loog_request(code)
        if message is None:
            if code in self.responses:
                message = self.responses[code][0]
            else:
                message = ''
        if self.request_version != 'HTTP/1.0':
            self.wfile.write("%s %d %s\r\n" % (self.protocol_version, code, message))
        self.seb