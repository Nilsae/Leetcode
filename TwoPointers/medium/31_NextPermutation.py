import numpy as np
# 1. Start from the end of the array:
#    Find the first index i where nums[i] < nums[i + 1]
#    (This is the "pivot" — where the order starts descending)

# 2. If such i does not exist:
#    The entire array is in descending order → reverse it and return

# 3. Otherwise:
#    From the end of the array again, find the first index j where nums[j] > nums[i]

# 4. Swap nums[i] and nums[j]

# 5. Reverse the subarray nums[i + 1:] (to make it the smallest possible)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot_idx = -1
        for idx in range(len(nums)-1, 0, -1):
            if nums[idx-1] < nums[idx]:
                pivot_idx = idx-1
                break
        if pivot_idx == -1:
            nums.reverse()
            return
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] >  nums[pivot_idx]:
                nums[idx], nums[pivot_idx] = nums[pivot_idx] , nums[idx]
                nums[pivot_idx + 1:] = reversed(nums[pivot_idx + 1:])
                break
    
print(Solution().nextPermutation(nums = [1,3, 2]))

# # Example 1:

# # Input: nums = [1,2,3]
# # Output: [1,3,2]
# # Example 2:

# # Input: nums = [3,2,1]
# # Output: [1,2,3]
# # Example 3:

# # Input: nums = [1,1,5]
# # Output: [1,5,1]