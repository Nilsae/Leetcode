class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if s[s_pointer]>= g[g_pointer]:
                s_pointer += 1
                g_pointer += 1
            else:
                s_pointer += 1
        return g_pointer
g = [10,9,8,7]
s =  [5,6,7,8]


# g = [1,2]
# s = [1,2,3]
print(Solution().findContentChildren(g, s))