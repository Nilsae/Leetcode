class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        hashmap2 = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]]!= t[i]:
                    return False
            hashmap[s[i]] = t[i]

            if t[i] in hashmap2:
                if hashmap2[t[i]]!= s[i]:
                    return False
            hashmap2[t[i]] = s[i]
            

        return True
print(Solution().isIsomorphic(s = "egg", t = "add")    )
print(Solution().isIsomorphic(s = "foo", t = "bar")           )    
print(Solution().isIsomorphic(s = "badc", t = "baba")           )    

           