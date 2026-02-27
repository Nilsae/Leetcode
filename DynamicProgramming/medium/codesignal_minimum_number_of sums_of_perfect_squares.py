def solution(n):
    arr = [1000000 for i in range(n+2)]
    arr[0] = 0
    perfect_sqs = []
    for i in range(1, int(n**0.5) + 1):
        perfect_sqs.append(i**2)
        arr[i**2] = 1
    for num in range(1, n + 1):
        for idx in perfect_sqs:
            if num - idx >= 0:
                arr[num] = min(arr[num], 1 + arr[num - idx])

    return arr[n]
    
    
solution(5)