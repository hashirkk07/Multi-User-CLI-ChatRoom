import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',5555))

alias = ""

def acceptMsg():
    while True:
        try:
            msg= client.recv(1024).decode('ascii')
            if msg == 'Enter your alias:':
                global alias 
                alias = input(msg)
                client.send(alias.encode('ascii'))
            else:
                print(msg)
        except:
            print('Error!!')
            client.close()
            break

def userInput():
    while True:
        msg = f'{alias}: {input("")}'
        client.send(msg.encode('ascii'))

acceptMsgThread = threading.Thread(target=acceptMsg)
acceptMsgThread.start()

userInputThread = threading.Thread(target=userInput)
userInputThread.start()
