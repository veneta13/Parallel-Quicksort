# Parallel Quicksort

## Introduction
The program implements an application that uses a parallel quicksort algorithm with a randomly generated pivot to sort lists submitted by clients to the server.

A method is also implemented to detect the time required to execute the algorithm from a different number of processes.


## Files

- **client.py** - contains client implementation
- **server.py** - contains server implementation
- **quicksort_parallel.py** - contains a parallel quicksort implementation
- **quicksort_sequential.py** - contains an implementation of sequential quicksort
- **time_quicksort.py** - contains an implementation of the detection of the time required for the execution of the algorithm

## Functions

### **client.py**

#### ```create_client(server_host, server_port)```

Creates a client that connects to the server at the address passed as parameters

#### ```send_client(client, message)```

Sends a message to the server

#### ```receive_client(client)```

Receives a message from the server

#### ```client_user_input()```

Allows the user to enter the number of processes and the list to be sorted

#### ```main()```

Starts the client on the specified host and port

### **server.py**

#### ```quicksort_helper(input_list, proc_count)```

Helper function for starting the quicksort algorithm

#### ```create_server(host, port)```

Creates a server at the address passed as parameters

#### ```serve(server)```

Uses Selector to serve customers

#### ```main()```

Starts the server on the specified host and port

### **quicksort_parallel.py**

#### ```quicksort_parallel(arr, p_pipe, num_max_proc, num_current_proc)```

A parallel implementation of the quicksort algorithm

### **quicksort_sequential.py**

#### ```quicksort_sequential(arr)```

Sequential implementation of the quicksort algorithm

### **time_quicksort.py**

Determines the execution time of the algorithm on arrays with 1000, 10 000, 100 000, 1 000 000, 10 000 000, 100 000 000 randomly generated elements with different number of processes.

## Notes

### Sample Output

[Sample output of runtime detection on _Intel Core i7-7700HQ_](result.txt)

### Resources
- [Demystifying Python Multiprocessing and Multithreading](https://towardsdatascience.com/demystifying-python-multiprocessing-and-multithreading-9b62f9875a27)

- [Socket Programming HOWTO](https://docs.python.org/3.10/howto/sockets.html)

- [LINUX PROGRAMMING - GETTING STARTED WITH THE SELECT MODEL](https://www.topcoder.com/thrive/articles/Linux%20Programming%20-%20Getting%20Started%20with%20the%20Select%20Model)
