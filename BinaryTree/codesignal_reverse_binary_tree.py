# Given a binary tree, write a function in Python to reverse the given binary tree. This means that for every node in the binary tree, you have to swap its left and right child nodes.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reverse_tree(root):
    if not root:
        return
    left_rev = reverse_tree(root.left)
    right_rev = reverse_tree(root.right)
    root.right = left_rev
    root.left = right_rev
    return root