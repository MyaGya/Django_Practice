from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):    # 핸들러 클래스를 상속받아 기본 기능만을 구현합니다
    def do_GET(self):
        self.send_response_only(200, 'OK') # 특이 체크 없이 무조건 200명령만 허용합니다
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World") # 바이트 문자열을 뜻합니다 기본적으로 인코딩 / 디코딩 과정을 거치기떄문에 인코딩된 문자를 클라이언트에 보내준다

if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler) # 서버의 IP, PORT가 기본값이 됩니다
    print("Started WevServer on port 8888...")
    print("Press ^C to quit WebServer.")
    server.serve_forever()          # 서버를 실행합니다