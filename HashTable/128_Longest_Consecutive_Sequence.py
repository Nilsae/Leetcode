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