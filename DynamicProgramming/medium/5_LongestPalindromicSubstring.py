class Solution(object):
    def func(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            s1 = self.func(s, i, i)   # odd
            s2 = self.func(s, i, i+1)  # even
            if len(s2) > len(s1):
                ans_ = s2
            else:
                ans_ = s1
            if len(ans_) > len(ans):
                ans = ans_
        return ans

print(Solution().longestPalindrome(s = "vagfafgav"))
                    
                
                             
            