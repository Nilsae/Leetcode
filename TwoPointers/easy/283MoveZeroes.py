class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = set()
        num_moved = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.add(i)
        for i in range(len(nums)):
            if i in zeros:
                for j in range(i + 1 - num_moved, len(nums)):
                    nums[j - 1] = nums[j]
                num_moved += 1
        for i in range(len(nums) - 1, len(nums) - 1 - len(zeros), -1 ):
            nums[i] = 0
