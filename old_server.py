import socket
from _thread import *
import sys

# server = "192.168.0.106"
server = "192.168.0.102"
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()  # 4 means maximum 4 users can connect to server; if left empty means unlimited
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode()
            print(reply)

            # if not data:
            #     print("Disconnected")
            #     break
            # else:
            #     print("Received: ", reply)
            #     print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    conn.send('Thank you for connecting'.encode())

    start_new_thread(threaded_client, (conn,))  # we don't want to wait for this function to execute, so we run it in the background using threads.
