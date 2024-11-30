class Solution(object):
    def twoSumNaive(self, nums, target):
        """
        :type nums: List[int]s
        :type target: int
        :rtype: List[int]
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        for idx, val in enumerate(nums):
            for idx1, val1 in enumerate(nums):
                if idx1!= idx and val + val1 == target:
                    return [idx, idx1]
        

    def twoSum(self, nums, target):
        """
        :type nums: List[int]s
        :type target: int
        :rtype: List[int]
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        hashmap = {}

        for idx, val in enumerate(nums):
            complement = target - nums[idx]
            if complement in hashmap:
                return [hashmap[complement], idx]
            else:
                hashmap[val] = idx
            
print(Solution().twoSum(nums = [2,7,11,15], target = 9))