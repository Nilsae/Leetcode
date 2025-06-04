class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans =0
        window_size = 2
        while window_size<= len(nums):
            for right in range(window_size, len(nums)):
                if nums[right-1] - nums[right-2] == nums[right] - nums[right-1]:
                    ans +=1
                else: 
                    break
            window_size += 1
        return ans
print(Solution().numberOfArithmeticSlices(nums = [1,2,3,4]))
    # An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:

# Input: nums = [1]
# Output: 0