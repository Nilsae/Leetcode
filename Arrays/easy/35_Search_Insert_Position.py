import math
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        return self.helper_func_recursive(nums, target, 0, len(nums) - 1)
    def helper_func_recursive(self, nums, target, left, right):
        # print(mid, nums)
        mid = (left+ right) // 2
        if left > right:
            return left
        if target <  nums[mid]:
            return self.helper_func_recursive(nums, target, left, mid -1 )
        elif target > nums[mid]:
            return self.helper_func_recursive(nums, target, mid +1 , right)
        else:
            return mid
    def helper_func_iterative(self, nums, target, left, right):
        while(left<=right):
            mid = (left+ right) // 2
            if nums[mid] == target:
                return mid
            elif target <  nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid +1
        return left
        
# print(Solution().searchInsert(nums = [1,3,5,6], target = 7))
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4