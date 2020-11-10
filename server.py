import socket
import threading

host = '127.0.0.1'
port = 45454
clients = []
aliases = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

def broadcast(msg):
    for client in clients:
        client.send(msg)

def forward(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            clientNum = clients.index(client)
            clientAlias = aliases[clientNum]
            aliases.remove(clientAlias)
            clients.remove(client) 
            
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
        print(f'client {str(alias)} connected from the address {str(addr)}')
        client.send('You are connected to the room'.encode('ascii'))
        broadcast(f'User {str(alias)} entered the room using {str(addr)}'.encode('ascii'))

        thread = threading.Thread(target=forward, args=(client,))
        thread.start()

print('listening mode enabled')
clientConnect()




