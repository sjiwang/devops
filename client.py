from datetime import datetime
from socket import *
import time

from gotone import AliSms

IP = '192.168.3.21'
PORT = 10086
BUFLEN = 1024

time_format = '%Y-%m-%d %H:%M:%S'


def client_socket_connect():
    i = 0
    while True:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((IP, PORT))
            sock.send("hello world".encode())
            recved = sock.recv(BUFLEN)
            now_str = datetime.now().strftime(time_format)
            recved_str = recved.decode()
            print(f'{now_str},receive "{recved_str}"')

            # 如果没有这个程序，表示程序退出
            if 'StrategyFramework' not in recved_str:
                i = i + 1
                if i % 20 == 0:
                    AliSms().send_sms('192.168.3.21', 'StrategyFramework')

            time.sleep(10)
        except Exception as e:
            print(type(e))
            if isinstance(e, (ConnectionRefusedError, ConnectionResetError)):
                AliSms().send_sms('192.168.3.21', '系统')
                print('服务端异常')
            else:
                print('客户端异常')
            break


if __name__ == '__main__':
    client_socket_connect()
