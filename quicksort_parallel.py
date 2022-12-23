import random
from multiprocessing import Pipe, Process


def quicksort_sequential(arr):
    if len(arr) < 2:
        return arr

    pivot = arr.pop(random.randint(0, len(arr) - 1))

    left_arr = [item for item in arr if item < pivot]
    right_arr = [item for item in arr if item >= pivot]

    return quicksort_sequential(left_arr) + [pivot] + quicksort_sequential(right_arr)


def quicksort_parallel(arr, p_pipe, num_max_proc, num_current_proc):
    if len(arr) < 2 or num_current_proc > num_max_proc:
        p_pipe.send(quicksort_sequential(arr))
        p_pipe.close()
        return

    pivot = arr.pop(random.randint(0, len(arr) - 1))

    left_arr = [item for item in arr if item < pivot]
    right_arr = [item for item in arr if item >= pivot]

    left_p_pipe, left_c_pipe = Pipe()
    right_p_pipe, right_c_pipe = Pipe()

    left_proc = Process(
        target=quicksort_parallel,
        args=(
            left_arr,
            left_c_pipe,
            num_max_proc,
            num_current_proc - 1
        )
    )

    right_proc = Process(
        target=quicksort_parallel,
        args=(
            right_arr,
            right_c_pipe,
            num_max_proc,
            num_current_proc - 2
        )
    )

    left_proc.start()
    right_proc.start()

    p_pipe.send(left_p_pipe.recv() + [pivot] + right_p_pipe.recv())
    p_pipe.close()

    left_proc.join()
    right_proc.join()


def quicksort(arr, max_proc):
    assert max_proc > 0

    p_pipe, c_pipe = Pipe()

    proc = Process(
        target=quicksort_parallel,
        args=(
            arr,
            c_pipe,
            max_proc,
            1)
    )

    proc.start()
    print(p_pipe.recv())
    proc.join()


if __name__ == '__main__':
    quicksort([454, 54, 2, 0, -4, 45, 0, 8, -2], 1)
