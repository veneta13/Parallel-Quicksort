import math
import random
import time
from multiprocessing import Pipe, Process, cpu_count

from quicksort_parallel import quicksort_parallel


def main():
    test = [1000, 10000, 100000, 1000000, 10000000, 100000000]
    arrays = [[random.random() for x in range(test[case])] for case in range(len(test))]

    for proc_count in range(int(math.log2(cpu_count()))):
        for test_case in range(len(test)):
            time.sleep(2)

            p_pipe, c_pipe = Pipe(duplex=False)
            proc = Process(target=quicksort_parallel, args=(arrays[test_case], c_pipe, proc_count, 1))

            start = time.time()
            proc.start()
            p_pipe.recv()
            end = time.time()

            proc.join()
            proc.close()
            print(f'Time taken for {2 ** (proc_count + 1) if proc_count != 0 else 1} process(es) to sort array with {test[test_case]} members: {end - start}')
        print('---------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    main()