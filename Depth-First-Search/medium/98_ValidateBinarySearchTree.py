# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.DFS(root, 1000000000000, -1000000000000)
    def DFS(self, node,  left_max_range, right_min_range):
        if not node:
            return True
        if node.val>=left_max_range or node.val<=right_min_range:
            return False
        return self.DFS(node.left,  node.val, right_min_range) and self.DFS(node.right,  left_max_range, node.val)
          
# Solution().isValidBST(root = [2,1,3])
# Input: root = [2,1,3]
# Output: true
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.