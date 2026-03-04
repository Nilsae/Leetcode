# You are given an array of n integers and a number k. Your task is to calculate the number of distinct pairs in the array that have a difference of k. A pair consists of two integers that are different, and the absolute difference between the integers is exactly k.

# The solution is expected to have linear time complexity, i.e., 
# O(n).



from collections import Counter
def count_pairs_with_diff_k(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = set()
        d[nums[i]].add(i)
    ans = 0
    visited = set()
    for i in range(len(nums)):
        complement = nums[i] - k  # counts (a, b)
        if complement in d and i not in visited:
            for idx in d[complement]:
                if i != idx:
                    ans += 1
            visited.add(i)
        # complement = nums[i] + k  # counts (b, a) -> answer will be double what it should be
        # if complement in d:
        #     for idx in d[complement]:
        #         if i != idx:
        #             ans += 1
    return ans 

