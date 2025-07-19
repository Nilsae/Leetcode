# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        visited = set()
        self.ans = []
        depth = 0
        self.helper(root, visited, depth)
        
        max_depth = max(self.ans, key=lambda x: x[1])[1]
        output = [[] for i in range(max_depth+1)]
        for pair in self.ans:
            output[pair[1]].append(pair[0])
        for i in range(len(output)):
            if i%2 ==1:
                output[i].reverse()
        return output

        
    def helper(self, node, visited, depth):
        if not node or node in visited:
            return
        self.ans.append((node.val,depth))
        self.helper(node.left, visited, depth+1)
        self.helper(node.right, visited, depth +1)
        visited.add(node)
        