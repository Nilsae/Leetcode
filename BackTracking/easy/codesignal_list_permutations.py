# You are provided with an array of n integers, which may contain duplicate elements. Write a recursive function that generates all distinct permutations of the numbers in the array. The permutations need to be of the same length as the input array, and they should be in lexicographically sorted order.

# Use a method similar to backtracking to solve this task. The function should return an array of all these permutations. The expected time complexity for the solution is 

# O(N!).

# Note: You cannot use a built-in Python function or library method to directly generate permutations. The intention here is to specifically practice recursion and backtracking techniques.

def solution(nums):
    n = len(nums)
    # i = 0
    pers = []
    def bt(i):
        nonlocal pers
        if i == n:
            if nums not in pers:
                pers.append(nums[:])
        for first in range(i, n):
            nums[first], nums[i] = nums[i], nums[first]
            bt(i + 1)
            nums[first], nums[i] = nums[i], nums[first]
    bt(0)
    pers = sorted(pers)
        
    return pers