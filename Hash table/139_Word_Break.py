class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        true_set = set()
        true_set.add(0)
        for index in range(1, len(s)+1):
            for True_indx in true_set:
                if s[True_indx:index] in wordDict:
                    dp[index] = True
            if dp[index] == True:
                true_set.add(index)
            
        return dp[-1]
