import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

# Fazendo o servidor listar as conexões
server_socket.listen()

sockets_list = [server_socket]

# Lista de clientes conectados - socket usa cabeçalho e nome como dados
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

def receive_message(client_socket):

    try:

        # Recebe o cabeçalho contendo o tamanho da mensagem
        message_header = client_socket.recv(HEADER_LENGTH)

        # Se houver o recebimento da mensagem, fecha-se a conexão
        if not len(message_header):
            return False

        # Convertendo cabeçalho para um valor inteiro
        message_length = int(message_header.decode('utf-8').strip())

        # Retornando o objeto da mensagem de cabaçalho e os dados da mensagem
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:

        # Em caso de erro:
        return False

while True:

    
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


    # Iterate over notified sockets
    for notified_socket in read_sockets:

        # Se a notificação do socket é um servidor socket - nova conexão, aceita
        if notified_socket == server_socket:

            
            client_socket, client_address = server_socket.accept()

            
            user = receive_message(client_socket)

            
            if user is False:
                continue

           
            sockets_list.append(client_socket)

            
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        # Se o socket existente estiver enviando uma mensagem 
        else:

            # Recebendo a mensagem
            message = receive_message(notified_socket)

            # Se falso, cliente é desconectado
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                # Removendo da lista de sockets
                sockets_list.remove(notified_socket)

                # Removendo da lista de usuários
                del clients[notified_socket]

                continue

            # Passando o usuário que enviou a mensagem
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            
            for client_socket in clients:

                
                if client_socket != notified_socket:

                    # Usuário e respectiva mensagem
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # Exceções 
    for notified_socket in exception_sockets:

        # Remove da lista de sockets
        sockets_list.remove(notified_socket)

        # Remove da lista de usuários
        del clients[notified_socket]