import random
from multiprocessing import Pipe, Process

from quicksort_sequential import quicksort_sequential


def quicksort_parallel(arr, p_pipe, num_max_proc, num_current_proc):
    if len(arr) < 2 or num_current_proc > num_max_proc:
        p_pipe.send(quicksort_sequential(arr))
        p_pipe.close()
        return

    pivot = arr.pop(random.randint(0, len(arr) - 1))

    left_arr = [item for item in arr if item < pivot]
    right_arr = [item for item in arr if item >= pivot]

    left_p_pipe, left_c_pipe = Pipe(duplex=False)
    right_p_pipe, right_c_pipe = Pipe(duplex=False)

    left_proc = Process(
        target=quicksort_parallel,
        args=(
            left_arr,
            left_c_pipe,
            num_max_proc,
            num_current_proc * 2
        )
    )

    right_proc = Process(
        target=quicksort_parallel,
        args=(
            right_arr,
            right_c_pipe,
            num_max_proc,
            num_current_proc * 2
        )
    )

    left_proc.start()
    right_proc.start()

    p_pipe.send(left_p_pipe.recv() + [pivot] + right_p_pipe.recv())
    p_pipe.close()

    left_proc.join()
    right_proc.join()

    left_proc.close()
    right_proc.close()
