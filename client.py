import socket

from colorama import Fore, Style


def create_client(server_host, server_port):
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client.connect((server_host, server_port))

    return client


def send_client(client, message):
    print(Fore.BLUE + f'Sending a message: {message}')
    client.send(message.encode())


def receive_client(client):
    message = client.recv(1024).decode()

    if not message:
        client.close()
        return None

    print(Fore.GREEN + f'Received a message: {message}')
    print(Style.RESET_ALL)
    return message


def client_user_input():
    proc_count = int(input(Fore.MAGENTA + 'Enter process count: '))

    input_list = list(map(int, input(Fore.MAGENTA + 'Enter the list: ').strip().split()))

    result = '('
    result += str(proc_count)
    result += ', '
    result += '['
    result += ','.join([str(i) for i in input_list])
    result += '])'

    return result


def main():
    client = create_client('localhost', 8008)
    send_client(client, client_user_input())
    receive_client(client)


if __name__ == "__main__":
    main()
