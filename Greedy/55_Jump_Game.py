
import numpy as np
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_idx = 0
        while cur_idx < len(nums)-1:
            if not nums[cur_idx]:
                return False
            if cur_idx + nums[cur_idx] > len(nums) -1:
                return True
            if nums[cur_idx] == 1:
                cur_idx = cur_idx + 1
            else:
                sublist = nums[cur_idx+1: cur_idx+1+nums[cur_idx]]
                sublist = [sublist[i] + i for i in range(len(sublist))]
                max_idx_rev = len(sublist) -np.argmax(sublist[::-1]) - 1
                cur_idx = max_idx_rev+ cur_idx + 1
        return True
    def canJump_a_bit_faster(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = -1
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if i <max_idx:
                continue
            if not nums[i]:
                return False
            if i + nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 1:
                continue
            max_num = -1
            for j in range(i+1, i+1 + nums[i]):
                if nums[j]+ j >= max_num:
                    max_num = nums[j]+ j
                    max_idx = j
        return True
    def a_bit_more_efficient(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True
Solution().canJump(nums = [5,9,3,2,1,0,2,3,3,1,0,0])
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.