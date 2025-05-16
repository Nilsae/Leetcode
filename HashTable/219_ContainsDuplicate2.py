class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Tracking "left" : goes slightly faster
        seen = set()
        left = 0
        if k ==0:
            return False
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            if i == k + left:
                seen.remove(nums[left])
                left = left + 1
            seen.add(nums[i])
        return False
        # Tracking len(seen): prettier and neater but slightly slower
        # seen = set()
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen.add(nums[i])
        #     if len(seen) > k:
        #         seen.remove(nums[i-k])
        # return False
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false