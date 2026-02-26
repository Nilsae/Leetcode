def are_coprime(a, b):
    n = a
    if b > a:
        n = b
    # n = int(n ** 0.5)
    for i in range(2, n):
        while a % i == 0 and b % i == 0:
            a //= i
            b //= i
            return False
    return True

# This is simple. The efficient implementation is greatest common divisor (GCD) algorithm