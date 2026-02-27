# The task is related to climbing stairs. Imagine you have to climb n stairs, starting with the stair number 0. At each step, you can either climb 1 stair or 2 stairs. The task is to compute the total number of distinct ways you can climb the n stairs.

# For example, for n = 4, the output should be total_ways(n) = 5, as 4 = 1 + 1 + 1 + 1, 4 = 1 + 1 + 2, 4 = 1 + 2 + 1, 4 = 2 + 1 + 1, and 4 = 2 + 2, totalling to 5 different ways.



def total_ways(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = total_ways(n-1, memo) + total_ways(n-2, memo)
    return memo[n]