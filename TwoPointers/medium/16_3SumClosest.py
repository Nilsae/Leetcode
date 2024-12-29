class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2] 
        for i in range(n):
            left = i+1
            right = n - 1
            while left < right:
                current_sum = nums[left]+nums[right] + nums[i]
                if current_sum == target:
                    return target
                elif current_sum > target:
                    if current_sum - target < abs(closest - target):
                        closest = current_sum
                    right -= 1
                else:
                    if target - current_sum < abs(closest - target):
                        closest = current_sum
                    left += 1
            
        return closest


print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
