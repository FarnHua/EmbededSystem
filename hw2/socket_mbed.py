import socket
import numpy as np
import json
import time
import random


# Standard loopback interface address

# print(str((socket.gethostbyname("LAPTOP-SG8SBIN3"))))
print(socket.gethostbyname(socket.gethostname()))
HOST = "192.168.93.169"
PORT = 8000            # Port to listen on (use ports > 1023)
path = 'output.txt'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(s.getsockname())
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        count = 0
        with open(path, 'w', encoding='utf-8') as f:
            while count < 400:
                count += 1
                data = conn.recv(1024).decode('utf-8')
                f.write(data)
                f.write("\n")
                print('Received from socket server : ', data)
