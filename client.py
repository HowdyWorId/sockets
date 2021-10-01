import socket
import time

sock = socket.socket(family=socket.AF_INET,
              type=socket.SOCK_STREAM)
sock.connect(("192.168.1.101", 8082))
print('connected!')
while True:
    msg = input('Message\n')
    sock.send(msg.encode('utf-8'))
