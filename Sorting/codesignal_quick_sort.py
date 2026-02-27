def quicksort_custom(arr):
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return arr
    left = []
    right = []
    pivot = arr[0]
    for i in range(1, n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort_custom(left) + [pivot] + quicksort_custom(right)