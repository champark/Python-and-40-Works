import socket

in_addr = socket.gethostbyname(socket.gethostname())

# 컴퓨터의 내부 IP를 출력
print(in_addr)
