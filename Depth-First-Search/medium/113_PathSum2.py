# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.target_sum = targetSum
        self.helper(root, 0, [])
        return self.ans
    def helper(self, node, cur_sum, cur_path):
        if not node:
            return
        cur_sum+= node.val
        cur_path.append(node.val)
        if not node.right and not node.left and cur_sum == self.target_sum:
            self.ans.append(list(cur_path))
        self.helper(node.left, cur_sum, cur_path)
        self.helper(node.right, cur_sum, cur_path)
        # cur_sum -= node.val
        del cur_path[-1]
        return