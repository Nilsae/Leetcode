from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
        # s_cnt = Counter(s)
        # t_cnt = Counter(t)
        # for i in s_cnt:
        #     if not(i in t_cnt and s_cnt[i] == t_cnt[i]):
        #         return False
        # for i in t_cnt:
        #     if not(i in s_cnt and s_cnt[i] == t_cnt[i]):
        #         return False
        # return True