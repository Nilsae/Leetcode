# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        self.total_sum = 0
        visited = set()
        self.DFS(root, 0, visited)
        return self.total_sum
    def DFS(self, node, cur_num, visited):
        if node in visited or not node:
            return
        if not node.left and not node.right:
            cur_num = cur_num*10 + node.val
            self.total_sum+=cur_num
            return
        self.DFS(node.left, cur_num*10 + node.val, visited)
        self.DFS(node.right, cur_num*10 + node.val, visited)
        visited.add(node)
        