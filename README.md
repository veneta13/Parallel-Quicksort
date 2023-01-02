# Паралелен Quicksort

## Въведение
Програмата реализира приложение, което използва паралелен quicksort алгоритъм със случайно избран разделящ елемент за да сортира списъци, 
подадени от клиентите към сървъра.

Също е имплементиран метод за засичане на времето, необходимо за изпълнение на алгоритъма
от различен брой процеси.


## Файлове

- **client.py** - съдържа реализация на клиент
- **server.py** - съдържа реализация на сървър
- **quicksort_parallel.py** - съдържа реализация на паралелен quicksort
- **quicksort_sequential.py** - съдържа реализация на последователен quicksort
- **time_quicksort.py** - съдържа реализация на засичането на времето, необходимо за изпълнението на алгоритъма

## Функции

### **client.py**

#### ```create_client(server_host, server_port)```

Създава клиент, който се свързва към сървъра на подадения като параметри адрес

#### ```send_client(client, message)```

Изпраща съобщение на сървъра

#### ```receive_client(client)```

Получава съобщение от сървъра

#### ```client_user_input()```

Позволява на потребителя да въведе броя на процесите и списъка, който да бъде сортиран

#### ```main()```

Стартира клиента на указаните хост и порт

### **server.py**

#### ```quicksort_helper(input_list, proc_count)```

Помощна функция за стартирането на quicksort алгоритъма

#### ```create_server(host, port)```

Създава сървър на подадения като параметри адрес

#### ```serve(server)```

Използва Selector, за да обслужва клиентите

#### ```main()```

Стартира сървъра на указаните хост и порт

### **quicksort_parallel.py**

#### ```quicksort_parallel(arr, p_pipe, num_max_proc, num_current_proc)```

Паралелна реализиция на quicksort алгоритъма

### **quicksort_sequential.py**

#### ```quicksort_sequential(arr)```

Последователна реализиция на quicksort алгоритъма

### **time_quicksort.py**

Засича времето на изпъление на алгоритъма върху масиви с 1000, 10 000, 100 000,
1 000 000, 10 000 000, 100 000 000 случайно генерирани елементи с различен брой процеси.

## Допълнение

### Примерен изход

[Примерен изход от засичането на времето на изпълнение върху _Intel Core i7-7700HQ_](result.txt)

### Използвани източници:
- [Demystifying Python Multiprocessing and Multithreading](https://towardsdatascience.com/demystifying-python-multiprocessing-and-multithreading-9b62f9875a27)

- [Socket Programming HOWTO](https://docs.python.org/3.10/howto/sockets.html)

- [LINUX PROGRAMMING - GETTING STARTED WITH THE SELECT MODEL](https://www.topcoder.com/thrive/articles/Linux%20Programming%20-%20Getting%20Started%20with%20the%20Select%20Model)