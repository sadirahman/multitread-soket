import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 1234

clients = []


s.bind((ip, port))
s.listen()
print('Server Ready...')
print('Ip Address of the Server::%s'%ip)

def handleClient(client):
    while True:
        message = client.recv(1024)
        if (clients[0]==client):
            clients[1].send(message)
        else:
            clients[0].send(message)


while serverRunning:
    client,address = s.accept()
    print('%s connected to the server'%str(address))
    client.send('Welcome to messanger'.encode('ascii'))

    if (client not in clients):
        clients.append(client)
        threading.Thread(target=handleClient, args=(client,)).start()