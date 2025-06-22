# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        self.target_sum = targetSum
        self.ans = False
        self.helper(root, 0)
        return self.ans
    def helper(self, node, cur_sum):
        if not node:
            return
        cur_sum += node.val
        if not node.right and not node.left and cur_sum == self.target_sum:
            self.ans = True
        self.helper(node.left, cur_sum)
        self.helper(node.right, cur_sum)
        cur_sum -= node.val
        return