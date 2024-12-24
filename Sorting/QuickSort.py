#Naiive:
def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]  # pivot itself is in the middle of the list if there are no duplicates.
    right = [i for i in arr if i > pivot]
    return quicksort(left) + middle + quicksort(right)
    
        
        
print(quicksort(arr = [8,7,5,6,2,3,0,9,4,5]))
    