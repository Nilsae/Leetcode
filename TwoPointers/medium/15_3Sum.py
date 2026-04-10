class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i >0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = n - 1
            target = -nums[i]
            while left < right:
                if nums[left]+nums[right] == target:
                    sol = [nums[left] , nums[i], nums[right]]
                    res.append(sol)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            
        return res

# print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
print(Solution().threeSum(nums = [3,0,-2,-1,1,2]))



# new implementation:

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0 
        while i < n:
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    l = [nums[left], nums[right], nums[i]]
                    ans.append(l)
                    while left < n - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1
                    right -= 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
            
        return ans
