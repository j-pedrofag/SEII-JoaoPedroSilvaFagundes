import socket

s = socket.socket()
host = socket.gethostname()
port = 13245
s.bind((host,port))
s.listen(1)
print("Esperando conexão!")

connect_client, address = s.accept()
print("O cliente foi conectado")

file = open('file_server.txt', 'rb')
dados = file.read(1024)
connect_client.send(dados)
print("Os dados foram enviados")