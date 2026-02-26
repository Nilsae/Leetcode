def nth_prime(n: int) -> int:
    if n == 1:
        return 2
    if n == 2:
        return 3
    input_n = n
    nth = 2
    cur_n = 4
    while nth <= input_n:
        if is_prime(cur_n):
            nth += 1
            if nth == input_n:
                return cur_n
        cur_n += 1
# You don't need to handle n == 1 and n == 2 as special cases if you use a loop that starts from 2 and counts primes found.
# Instead of checking every number, you can skip even numbers after 2.
# You can store found primes and use them to speed up the is_prime check.