# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.p1 = self.p2 = None
        self. prev = None
        self.helper(root)
        if self.p1 and self.p2:
            self.p1.val, self.p2.val = self.p2.val, self.p1.val
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if (self.prev and node.val < self.prev.val) :
            if not self.p1:
                self.p1 = self.prev
            self.p2 = node
        self.prev = node
        self.helper(node.right)