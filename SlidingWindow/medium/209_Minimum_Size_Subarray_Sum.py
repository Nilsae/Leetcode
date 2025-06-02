class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # brute force:
        # for dif in range(len(nums)):
        #     for left in range(len(nums)-dif):
        #         if sum(nums[left:left+dif+1])>=target:
        #             return dif + 1
        # return 0
        
        min_len = len(nums) + 1
        left = 0
        rsum = 0
        for right in range(len(nums)):
            rsum += nums[right]
            if rsum>=target:
                while(rsum-nums[left]>=target):
                    rsum -= nums[left]
                    left = left + 1
                min_len = min(min_len, right - left + 1)

        return 0 if min_len == len(nums) + 1 else min_len
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
