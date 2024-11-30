class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s== "":
            return True
        flag = 0
        for i in range(len(t)):
            if s[flag] == t[i]:
                flag += 1
                if flag == len(s):
                    return True
        return False
                      
        
print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))