import socket
from queue import Queue

import select


def create_server(host, port):
    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Unset blocking
    server.setblocking(0)

    # Bind to host and port
    server.bind((host, port))

    server.listen()

    return server


def serve(server):
    # Wait until ready for reading list
    reads = [server]

    # Wait until ready for writing list
    writes = []

    # Wait for exceptional condition list
    errors = []

    # Message queue
    messages_per_client = {}

    while True:
        read_sel, write_sel, except_sel = select.select(reads, writes, errors)

        for obj in read_sel:
            if obj is server:
                # Accept the client
                connection, client = obj.accept()

                print(f'New client found: {client}')

                # Unset blocking
                connection.setblocking(0)

                # Add client to reads
                reads.append(connection)

                # Create message queue for current connection
                messages_per_client[client] = Queue()
            else:
                # Receive message
                message = obj.recv(1024)
                if message:

                    if obj not in messages_per_client.keys():
                        messages_per_client[obj] = Queue()

                    try:
                        print(eval(message))
                    except (ValueError, SyntaxError):
                        pass

                    messages_per_client[obj].put(message)

                    # Add to writes
                    if obj not in writes:
                        writes.append(obj)

        for obj in write_sel:
            try:
                message = messages_per_client[obj].get_nowait()
            except:
                writes.remove(obj)
            else:
                obj.send(message)


def main():
    server = create_server('localhost', 8008)
    serve(server)


if __name__ == "__main__":
    main()
