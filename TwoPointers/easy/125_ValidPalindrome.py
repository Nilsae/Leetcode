import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        left =0
        right  = len(s) -1
        while right - left> 0:
            if s[left]!= s[right]:
                return False
            left += 1
            right -= 1
            
        return True
print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))