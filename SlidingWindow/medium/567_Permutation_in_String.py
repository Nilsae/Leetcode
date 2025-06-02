from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]

            if window == s1_count:
                return True

        return False
                
print(Solution().checkInclusion(s1 = "adc", s2 = "dcda"))
# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false