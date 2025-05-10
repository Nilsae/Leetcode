class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return sum(nums)/float(k)
        max_sum = current_sum = sum(nums[i] for i in range(0, k))
        left = 1
        right = k
        while(right<len(nums)):
            prev_sum = current_sum
            current_sum = prev_sum - nums[left-1]+ nums[right]
            if current_sum > max_sum:
                max_sum = current_sum
            # max_sum = max(max_sum, current_sum)
            left = left + 1
            right = right + 1
        return max_sum/float(k)
print(Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000