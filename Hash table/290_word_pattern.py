class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = [i for i in s.split(" ")]
        # print(len(s))
        # print(len(pattern))
        pattern_to_s = {}
        s_to_pattern = {}
        for i in range(len(pattern)):
            if len(pattern) != len(s):
                return False
            # print(pattern_to_s)
            # print(s_to_pattern)

            if pattern[i] in pattern_to_s:
                if pattern_to_s[pattern[i]]!= s[i]:
                    return False
            pattern_to_s[pattern[i]] = s[i]
            
            if s[i] in s_to_pattern:
                if s_to_pattern[s[i]]!= pattern[i]:
                    return False
            s_to_pattern[s[i]] = pattern[i]
        return True
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))