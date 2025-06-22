# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if left_depth != 0 and  right_depth != 0:
            return min(left_depth, right_depth) + 1
        else:
            return max(left_depth, right_depth) + 1