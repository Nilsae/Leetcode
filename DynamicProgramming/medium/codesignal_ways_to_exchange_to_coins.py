# non-efficient: 
def coin_change(coins, amount, memo = None, start = 0):
    if memo is None:
        memo = {}
    if amount == 0:
        return 1
    if amount < 0 or start == len(coins):
        return 0
    
    key = (amount, start)
    if key in memo:
        return memo[key]
    ways = 0
    for i in range(start, len(coins)):
        ways += coin_change(coins, amount - coins[i], memo, i)
    memo[key] = ways

    return ways
    


#  iterative DP no recursion:
def coin_change(coins, amount, ways = None):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for i in range(len(coins)):
        for a in range(coins[i], amount + 1):
            ways[a] += ways[a - coins[i]]

    return ways[amount]
    
# trace of DP:
# Suppose coins = [1, 2] and amount = 4.

# Initialization:

# ways = [1, 0, 0, 0, 0] (since ways[0] = 1)
# First outer loop (i = 0, coin = 1):

# For a = 1: ways[1] += ways[0] → ways[1] = 1
# For a = 2: ways[2] += ways[1] → ways[2] = 1
# For a = 3: ways[3] += ways[2] → ways[3] = 1
# For a = 4: ways[4] += ways[3] → ways[4] = 1
# Now, ways = [1, 1, 1, 1, 1]
# Second outer loop (i = 1, coin = 2):

# For a = 2: ways[2] += ways[0] → ways[2] = 2
# For a = 3: ways[3] += ways[1] → ways[3] = 2
# For a = 4: ways[4] += ways[2] → ways[4] = 3
# Now, ways = [1, 1, 2, 2, 3]
# Result:

# ways[4] = 3 (There are 3 ways to make amount 4 with coins [1, 2])
