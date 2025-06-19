from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow= fast = 0
        n = len(nums)
        count = Counter(nums)
        print(count)
        flag = 0
        for fast in range(1, n):
            if nums[slow] != nums[fast]:
                if fast - slow > 2:
                    slow += 2
                    nums[slow] = nums[fast]
                    if count[nums[slow]] == 1:
                        slow -= 1
                        flag =1
                elif flag:
                    print(fast)
                    slow += 1
                    nums[slow] = nums[fast]
                    if count[nums[slow]] == 1:
                        slow -= 1
                        flag =1
        print(nums)
        return slow +2
        
        
print(Solution().removeDuplicates([0, 0, 1, 1, 1,1, 2, 3, 3]))