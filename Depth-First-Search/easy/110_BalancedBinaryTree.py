# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.ans = True
        self.height(root)
        return self.ans
    def height(self, node):
        if not node:
            return 0 
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height)>1:
            self.ans = False
        return 1+ max(left_height, right_height)