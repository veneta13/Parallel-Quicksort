import argparse
import socket
from multiprocessing import Process, Pipe
from queue import Queue

import select
from colorama import Fore, Style

from quicksort_parallel import quicksort_parallel


def quicksort_helper(input_list, proc_count):
    p_pipe, c_pipe = Pipe(duplex=False)
    proc = Process(
        target=quicksort_parallel,
        args=(
            input_list,
            c_pipe,
            proc_count,
            1
        )
    )

    proc.start()
    output = p_pipe.recv()
    proc.join()
    proc.close()
    return output


def create_server(host, port):
    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Unset blocking
    server.setblocking(0)

    # Bind to host and port
    server.bind((host, port))

    # Listen
    server.listen()

    print(Fore.BLUE + f'Listening on {host}:{port}' + Style.RESET_ALL)

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

                print(Fore.GREEN + f'New client found: {client}' + Style.RESET_ALL)

                # Unset blocking
                connection.setblocking(0)

                # Add client to reads
                reads.append(connection)

                # Create message queue for current connection
                messages_per_client[connection] = Queue()
            else:
                # Receive message
                message = obj.recv(1024)
                if message:
                    if obj not in messages_per_client.keys():
                        print(Fore.RED + 'Client not registered' + Style.RESET_ALL)
                        continue
                    try:
                        message_eval = eval(message)

                        if not isinstance(message_eval, tuple) or not isinstance(message_eval[1], list):
                            print(Fore.YELLOW + 'Please provide input in the following format:')
                            print(Fore.YELLOW + '(<number of processes>, <list to sort>)')
                            print(Style.RESET_ALL)
                        else:
                            # Sort the list
                            sorted_list = quicksort_helper(message_eval[1], message_eval[0])
                            # Put message into message queue
                            messages_per_client[obj].put('[' + ','.join([str(i) for i in sorted_list]) + ']')
                    except (ValueError, SyntaxError):
                        print(Fore.YELLOW + 'Please provide input in the following format:')
                        print(Fore.YELLOW + '(<number of processes>, <list to sort>)')
                        print(Style.RESET_ALL)

                    # Add client to writes
                    if obj not in writes:
                        writes.append(obj)

        for obj in write_sel:
            try:
                # Get message for current client
                message = messages_per_client[obj].get_nowait()
            except:
                # If there are no massage for that client remove from writes
                writes.remove(obj)
            else:
                # If there are messages waiting send them
                obj.send(message.encode())

        for obj in except_sel:
            if obj in reads:
                reads.remove(obj)
            if obj in writes:
                writes.remove(obj)
            obj.close()


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-sh", "--server_host", type=str, default='localhost', help="Host name")
    argParser.add_argument("-sp", "--server_port", type=int, default='8008', help="Port number")
    args = argParser.parse_args()

    server = create_server(args.server_host, args.server_port)
    serve(server)


if __name__ == "__main__":
    main()
