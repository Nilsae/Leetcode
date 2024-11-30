class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        highest_frequency = -1
        highest_frequent = nums[-1]
        for index, num in enumerate(nums):
            if num in dict:
                dict[num]+=1
            else:
                dict[num] = 1
            if dict[num]>highest_frequency:
                highest_frequency = dict[num]
                highest_frequent = num
        return highest_frequent
        
print(Solution().majorityElement(nums =
[3,3,4]))