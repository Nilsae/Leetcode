import numpy as np
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_arg = np.argmin(arr[i:]) + i
        min_elem = arr[min_arg]
        arr[min_arg] = arr[i]
        arr[i] = min_elem
    return arr
print(selection_sort([3, 1, 2, 4, 5]))