import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 내부, 외부 IP를 한 번에 출력
print("내부 IP : ", in_addr.getsockname()[0])
print("외부 IP : ", out_addr) 