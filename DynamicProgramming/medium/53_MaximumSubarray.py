class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return []
        left = 0
        right = 0
        max_sum = nums[0]
        current_sum = nums[0]
        r = l = 0
        for right in range(1, len(nums)):
            if current_sum < 0:
                current_sum = nums[right]
                left = right
            else:
                current_sum += nums[right]
            
            if current_sum > max_sum:
                max_sum = current_sum
                r = right
                l = left
            
        # print(nums[l:r+1])
        return max_sum
        
        
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))