# You are given an array of integers and an integer k. Your task is to determine whether there are two distinct indices, i and j, in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k. Return True if such a pair exists and False if not.

# The expected time complexity is 
# O(n), where 
# n is the length of the array.

def solution(nums, k):
    s = {}
    for i in range(len(nums)):
        if nums[i] not in s:
            s[nums[i]] = i
        else:
            j = s[nums[i]]
            if abs(i - j) <= k:
                return True
    return False
    
