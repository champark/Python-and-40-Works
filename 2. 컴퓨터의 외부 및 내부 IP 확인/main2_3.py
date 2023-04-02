import requests
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 컴퓨터 외부 IP를 알아보는 코드 만들기
print(out_addr)