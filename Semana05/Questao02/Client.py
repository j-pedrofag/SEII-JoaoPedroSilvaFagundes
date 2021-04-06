import socket
import select
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

# Declarando o username e codificando-o
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    # Espernado o usuário digitar a mensagem
    message = input(f'{my_username} > ')

    # Se a mensagem não for vazia:
    if message:

        # Condificando a mensagem em bytes
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # Loop para receber as mensagens
        while True:

            # Recebendo o cabeçalho com o tamanho da string username
            username_header = client_socket.recv(HEADER_LENGTH)

            # Se não receber nenhum dado, o servidor encerra a conexão
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convertendo o cabeçalho para valores inteiros
            username_length = int(username_header.decode('utf-8').strip())

            # Recebendo e decodificando o username
            username = client_socket.recv(username_length).decode('utf-8')

            # Repetindo o processo para a mensagem
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Printando a mensagem
            print(f'{username} > {message}')

    except IOError as e:
        # Em caso de erros:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

    
        continue

    except Exception as e:
       
        print('Reading error: '.format(str(e)))
        sys.exit()