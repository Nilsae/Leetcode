class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        sol = [nums[i], nums[j], nums[left], nums[right]]
                        res.append(sol)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        left += 1
        return res
    
print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))