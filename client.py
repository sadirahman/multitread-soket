import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

username =input('Enter user name::')

ip = input('Enter the IP Address::')
s.connect((ip,port))

def receiveMsg(sock):
    while True:
        message = sock.recv(1024).decode('ascii')
        print(message)

threading.Thread(target=receiveMsg,args=(s,)).start()

while True:
    tempmsg = input()
    message = username + '>>' + tempmsg
    s.send(message.encode('ascii'))