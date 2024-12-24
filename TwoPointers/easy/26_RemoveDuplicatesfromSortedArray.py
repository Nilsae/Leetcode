class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        slow = fast = 0
        for fast in range(1, n):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
print(Solution().removeDuplicates( nums = [0,0,1,1,1,2,2,3,3,4, 4]))