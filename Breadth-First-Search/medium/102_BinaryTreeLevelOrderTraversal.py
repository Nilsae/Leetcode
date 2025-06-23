# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        self.ans = []
        visited = set()
        self.helper(root, visited, 0)
        if not root:
            return []
        max_second = max(self.ans, key=lambda x: x[1])[1]
        answer = [[] for i in range(1+max_second)]
        for pair in self.ans:
            answer[pair[1]].append(pair[0])
        return answer
    def helper(self, node, visited, depth):
        if not node or node in visited:
            return
        self.ans.append((node.val,  depth))
        self.helper(node.left, visited, depth+1)
        self.helper(node.right, visited, depth+1)
        visited.add(node)
        return 

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []