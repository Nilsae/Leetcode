class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_binary_search_tree(root: TreeNode) -> bool:
    is_bst = True
    def func(root, min_allowed, max_allowed):
        nonlocal is_bst
        if not root:
            return
        if root.val < min_allowed or root.val > max_allowed:
            is_bst = False
        func(root.left, min_allowed, min(root.val, max_allowed))
        func(root.right, max(root.val, min_allowed), max_allowed)
    min_allowed = -float('inf')
    max_allowed = float('inf')
    func(root, min_allowed, max_allowed)
    if not root or (not root.left and not root.right):
        return True
    return is_bst