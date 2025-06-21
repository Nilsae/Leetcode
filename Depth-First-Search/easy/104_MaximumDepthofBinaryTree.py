# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my first try:
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        m = 0
        self.DFS(root, m)
        return self.ans
    def DFS(self, node, m):
        if not node: 
            m = 0
            return
        m+=1
        if self.ans< m:
            self.ans = m
        self.DFS(node.left, m)
        self.DFS(node.right, m)
        
#compact version:
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right)) 

