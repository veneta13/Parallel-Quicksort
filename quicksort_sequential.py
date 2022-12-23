import random


def quicksort_sequential(arr):
    if len(arr) < 2:
        return arr

    pivot = arr.pop(random.randint(0, len(arr) - 1))

    left_arr = [item for item in arr if item < pivot]
    right_arr = [item for item in arr if item >= pivot]

    return quicksort_sequential(left_arr) + [pivot] + quicksort_sequential(right_arr)
