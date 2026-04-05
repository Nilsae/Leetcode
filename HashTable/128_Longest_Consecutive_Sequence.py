class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # If the list is empty, return 0
        nums = set(nums)
        s = set()
        length = 1
        for i in nums:
            if i-1 not in nums:
                s.add(i)
        for initial in s:
            current_length = 1               
            while initial+1 in nums:
                current_length += 1
                initial += 1
            length = max(length, current_length)  # Update the maximum length if current length is longer
        return length   
               

        
        
        
        
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# new
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        if n == 0 or n == 1:
            return n
        nums.sort()
        max_len = 1
        l = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                l += 1
                max_len = max(l, max_len)
            elif nums[i] != nums[i - 1]:
                l = 1
        return max_len
