import socket

import select


def create_server(host, port):
    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Unset blocking
    server.setblocking(0)

    # Bind to host and port
    server.bind((host, port))

    return server


def serve(server):
    # Wait until ready for reading list
    reads = [server]

    # Wait until ready for writing list
    writes = []

    # Wait for exceptional condition list
    errors = []

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


def main():
    server = create_server('localhost', 8008)
    serve(server)


if __name__ == "__main__":
    main()
