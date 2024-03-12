from datetime import datetime
from socket import *
import time

IP = '192.168.3.21'
PORT = 10086
BUFLEN = 1024

time_format = '%Y-%m-%d %H:%M:%S'


def client_socket_connect():
    while True:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((IP, PORT))
            sock.send("hello world".encode())
            recved = sock.recv(BUFLEN)
            now_str = datetime.now().strftime(time_format)

            print(f'{now_str},receive "{recved.decode()}"')
            time.sleep(10)
        except Exception as e:
            print(type(e))
            if isinstance(e, (ConnectionRefusedError, ConnectionResetError)):
                print('服务端异常')
            else:
                print('客户端异常')
            break


if __name__ == '__main__':
    client_socket_connect()
