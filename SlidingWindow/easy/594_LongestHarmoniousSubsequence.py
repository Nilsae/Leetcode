
from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        final_result = 0
        for num in counter.keys():
            if counter[num + 1] == 0 and counter[num - 1] ==0:
                continue
            final_result = max(final_result, counter[num] + counter[num + 1], counter[num] + counter[num - 1])
        return final_result
print(Solution().findLHS(nums = [-3,-1,-1,-1,-3,-2]))
# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.