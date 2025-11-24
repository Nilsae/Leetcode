# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         gen_cnt = int(n * (n-1) )
#         dp = [[1 for i in range(n*2)] for j in range(gen_cnt)]
#         for i in range(gen_cnt):
#             dp[i][0] = 1
#         not_flag = -1
        
        
#         for i in range(gen_cnt):
#             for j in range(1, n*2-1):
#                 if sum(dp[i])== n:
#                     dp[i][j] = -1
#                 elif sum(dp[i])== 0:
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = dp[i-1][j] *not_flag
#                 not_flag *= -1
#         for i in range(gen_cnt):
#             dp[i][-1] = - sum(dp[i])
#         print(dp)
            
            
# Solution().generateParenthesis(n= 3)
        
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]