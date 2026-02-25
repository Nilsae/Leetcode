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





