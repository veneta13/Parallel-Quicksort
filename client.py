import socket


def create_client(server_host, server_port):
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client.connect((server_host, server_port))

    return client


def send_client(client, message):
    print(f'Sending a message: {message}')
    client.send(message.encode())
