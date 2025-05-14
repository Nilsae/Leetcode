class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.helper(s, 0, len(s) - 1, 1)
    def helper(self, s, left, right, tolerance):
        while left <= right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            elif tolerance:
                if right - left <= 1:
                    return True
                else: 
                    return self.helper(s, left+1, right, 0) or self.helper(s, left, right - 1, 0)
            else:
                return False
        return True
print(Solution().validPalindrome( s = "abbcca"))
# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false