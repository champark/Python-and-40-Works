import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))

# 컴퓨터의 내부 IP 확인. sockect으로 외부 사이트에 접속하고 접속된 정보를 바탕으로 IP를 확인하는 방법
print(in_addr.getsockname()[0])
