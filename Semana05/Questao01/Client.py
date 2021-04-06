import socket

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 13245
s.connect((host,port))
print("Conectado com sucesso!")

nome_do_arquivo_destino = input(str("Por favor, digite aqui o nome do arquivo destino: "))
filename = 'file_client %s %d %s.txt' %(ip,port,nome_do_arquivo_destino)
file = open(filename, 'wb')
dados = s.recv(1024)
file.write(dados)
file.close()
print("Os arquivos foram recebidos")