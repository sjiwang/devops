import datetime
from socket import *
import psutil

IP = '0.0.0.0'
PORT = 10086
BUFLEN = 1024

time_format = '%Y-%m-%d %H:%M:%S'


def get_python_process():
    processes = []
    for proc in psutil.process_iter():
        try:
            if 'python' in proc.name().lower() and proc.is_running():
                path = " ".join(proc.cmdline())
                processes.append(path)
        except:
            print('获取python进程失败')

    return processes


def server_socket_connect():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(5)

    while True:
        clientSocket, addr = sock.accept()
        recved = clientSocket.recv(BUFLEN)
        now_str = datetime.datetime.now().strftime(time_format)

        print(f'{now_str} from {addr} receive "{recved.decode()}"')
        processes = get_python_process()
        proc_str = ';'.join(processes)
        clientSocket.send(f'{proc_str}'.encode())
        clientSocket.close()


if __name__ == '__main__':
    server_socket_connect()
