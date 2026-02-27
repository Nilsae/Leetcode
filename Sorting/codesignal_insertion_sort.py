def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr