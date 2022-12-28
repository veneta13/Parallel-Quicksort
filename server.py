import select
import socket
import sys
import queue

def create_server(host, port):
    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Unset blocking
    server.setblocking(0)

    # Bind to host and port
    server.bind((host, port))

    return server
