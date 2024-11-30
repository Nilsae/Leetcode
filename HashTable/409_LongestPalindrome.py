class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = set()
        length = 0
        for i in range(len(s)):
            if s[i] in h:
                h.remove(s[i])
                length += 2
            else:
                h.add(s[i])
        return length +(len(h)>0)
        
        
        
print(Solution().longestPalindrome(s = "abccccdd"))
        
        
        
        
# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.