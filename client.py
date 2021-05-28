import json
import socket
import threading
import time

nick = input('write ur Nick:\n')

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=0, fileno=None)
# sock.connect(('127.0.0.100', 8081))
sock.connect(('192.168.1.101', 8081))

base_data = {'nick': nick, 'from': sock.getsockname()}


# /        if data.decode('utf-8') == 'is_connect':
#             sock.send('connected'.encode('utf-8'))
def send_data(data):
    sock.send(json.dumps(data).encode('utf-8'))


def steal_alive():
    b = True
    data = {'type': 'connection', 'new_connection': b, **base_data}

    while True:
        send_data(data)
        data['new_connection'] = False
        time.sleep(2)


def recieve():
    while True:
        data = sock.recv(1024)
        data = json.loads(data.decode('utf-8'))
        print(data.__str__())


def send():
    inp = str(input())
    data = {'type': 'msg', 'nick': nick, 'text': inp, 'from': sock.getsockname()}
    send_data(data)


def mainloop():
    while 1:
        send()
        # msg = f'{nick} says: {str(input(""))}'
        # sock.send(msg.encode('utf-8'))


threading.Thread(target=steal_alive).start()
threading.Thread(target=recieve).start()
if __name__ == '__main__':
    mainloop()
