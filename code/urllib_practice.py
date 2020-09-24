from urllib.parse import urlparse

result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")

print("urlparse의 인스턴스\n",result)


from urllib.request import urlopen
f = urlopen("http://www.example.com")
print("urlopen의 인스턴스",f.read(500).decode('utf-8'))