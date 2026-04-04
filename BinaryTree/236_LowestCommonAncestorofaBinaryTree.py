# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(node, target, path = None):
            if not node:
                return 
            if path == None:
                path = []
            
            if target == node:
                return path + [node]
            left_path = f(node.left, target, path + [node])
            if left_path:
                return left_path
            right_path = f(node.right, target, path + [node])
            if right_path:
                return right_path
        pp = f(root, p)
        pq = set(f(root, q))
        for node in pp[::-1]:
            if node in pq:
                return node
       
        
            