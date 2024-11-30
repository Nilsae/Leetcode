class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = end = 0
        hashmap = {}
        for end, val in enumerate(s):
            if val in hashmap and hashmap[val] >= start:
                start = hashmap[val] + 1
            max_len = max(max_len, end - start +  1)
            hashmap[val] = end
        return max_len
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
