def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    return n * factorial(n-1, memo)