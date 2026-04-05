from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        max_rep = 0
        ans = nums[0]
        for elem , rep in cnt.items():
            if rep > max_rep:
                ans = elem
                max_rep = rep
        return ans
    

# new:
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.items(), key = lambda x: x[1])[0]