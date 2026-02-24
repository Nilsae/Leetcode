def get_prime_factors(n):
    out_set = set()
    while n % 2 == 0:
        out_set.add(2)
        n //= 2
    for i in range(3, n+1, 2):
        while n % i == 0:
            out_set.add(i)
            n //= i
    if n > 1:
        out_set.add(n)
    return sorted(list(out_set))


# This is simple. The efficient implementation is greatest common divisor (GCD) algorithm
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