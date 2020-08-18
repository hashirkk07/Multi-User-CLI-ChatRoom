import socket
import threading

host = '127.0.0.1'
port = 45454
clients = []
aliases = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

def broadcast(mesg):
    for client in clients:
        client.send(mesg)

def forward(client):
    while True:
        try:
            mesg = client.recv(1024)
            broadcast(mesg)
        except:
            clientNum = clients.index(client)
            clientAlias = aliases[clientNum]
            clients.remove(client)
            aliases.remove(clientAlias)
            client.close()
            broadcast(f'User {clientAlias} has left from the room'.encode('ascii'))
            break

def clientConnect():
    while True:
        client, addr = server.accept()
        clients.append(client)
        client.send('Enter your alias:'.encode('ascii'))
        alias = server.recv(1024).decode('ascii')
        aliases.append(alias)
        print(f'client {alias} connected from the address {addr}')
        client.send('You are connected to the room'.encode('ascii'))
        broadcast(f'User {alias} entered the room using {addr}'.encode('ascii'))

        thread = threading.Thread(target=clientConnect, args=(client,))
        thread.start()

print('listening mode')


