from urllib.parse import urlparse

result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")

print("urlparse의 인스턴스\n",result)


from urllib.request import urlopen
f = urlopen("http://www.example.com")
print("urlopen의 인스턴스",f.read(500).decode('utf-8'))

### Django로 만든 임시 서버를 통한 POST 명령어의 실험 ###



print("="*50, "\n" "POST 방식 테스트 시작\n","="*50)


from urllib.request import urlopen
data = "language=python&framework=django"
f = urlopen("http://127.0.0.1:8000", bytes(data, encoding='utf-8'))
print(f.read(1000).decode('utf-8'))

from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = "http://127.0.0.1:8000"
data = {
    'name': '정찬영',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com'
}
encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data=postData)
#req.add_handler('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(500).decode('utf-8'))


