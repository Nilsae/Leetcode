class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        needle_idx = 0
        while left + len(needle) <= len(haystack):
            i = left
            while(haystack[i] ==  needle[needle_idx]):
                needle_idx = needle_idx + 1
                i = i + 1
                if needle_idx == len(needle):
                    return left
            left = left + 1
            needle_idx = 0
        return -1
    def cleaner_strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
# print(Solution().strStr("mississippi", needle = "pi"))
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.