class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # min_str_len = min(len(s) for s in strs) HAS OVERHEAD!
        min_str_len = 10000000
        for str in strs:
            if len(str)<min_str_len:
                    min_str_len = len(str) 
        # the above chunk beats 100%! interesting!
        if min_str_len == 0:
            return ""
        for common_idx in range(min_str_len):
            common = strs[0][common_idx]
            for s in strs:
                if s[common_idx]!= common:
                    return s[:common_idx]
        return strs[0][:min_str_len]
print(Solution().longestCommonPrefix(strs = ["flower","flower","flower","flower"]))
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.