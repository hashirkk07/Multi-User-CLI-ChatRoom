import socket
import threading

host = '127.0.0.1'
port = 87878

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(host,port)