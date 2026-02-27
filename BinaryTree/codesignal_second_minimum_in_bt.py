# Imagine we are given a binary tree in which each node contains an integer. Your task is to write a Python function that traverses this binary tree and returns the second smallest value among all the tree nodes. If there's no second smallest number (for example, if all the values in the tree are the same, or if there's only one node in the tree), the function should return None.

# You are not allowed to use sort() or any other built-in sorting methods in your solution. You should use Binary Tree Traversal techniques, which we have discussed in the lesson.

# Expected complexity is 

# O(n), where 
# n is the number of vertices in the binary tree. The expected additional memory is 
# O(1).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def second_minimum_in_tree(root):
    min1 = float('inf')
    min2 = float('inf')
    def func(root):
        nonlocal min1, min2
        if not root:
            return 
        func(root.left)
        if root.val < min1:
            min2 = min1
            min1 = root.val
        elif root.val < min2:
            min2 = root.val
        func(root.right)
    func(root)
    if min1 == min2 or min2 == float('inf'):
        return None
    return min2
    

