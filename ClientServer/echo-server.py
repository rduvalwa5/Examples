'''
Created on Jan 23, 2020

@author: rduvalwa2
'''

#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("binding host to port ", PORT)
    s.bind((HOST, PORT))
    print("starting listener")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print("No data")
                break
            conn.sendall(data)
            print("Sending Data ", data)