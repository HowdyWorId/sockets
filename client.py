import socket

sock = socket.socket(family=socket.AF_INET,
                     type=socket.SOCK_STREAM)
# sock.bind(("192.168.1.101", 8082))
sock.bind(("94.41.17.116", 8082))
print('Server started!')
class Data:
    data = []
    def __new__(cls, *args, **kwargs):
        return cls.data.append(args[0])

# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen()
while 1:
    conn, addr = sock.accept()
    print(addr)
    data = []
    while 1:
        _data = conn.recvfrom(2)
        if _data == b'':
            break
        print(_data)
        Data(_data) # just test ;)
        # data.append(_data)
    # print(data)
    print(Data.data)
