"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#inefficient version
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        visited = set()
        if not root:
            return root
        self.visit_list = []
        self.helper(root, visited, 0)
        max_depth = max(self.visit_list, key = lambda x :x[1])[1]
        node_depth = [[] for i in range(max_depth+1)]
        for pair in self.visit_list:
            node_depth[pair[1]].append(pair[0])
        for level in node_depth:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None
        return root
    def helper(self, node, visited, depth):
        if not node or node in visited:
            return
        self.visit_list.append((node, depth))
        self.helper(node.left, visited, depth+1)
        self.helper(node.right ,visited, depth+1)
        visited.add(node)
        
# efficient version:
# efficient version:
# efficient version:
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        head = root
        while head.left:
            cur = head
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                # else:
                #     cur.right.next = None
                cur = cur.next
            head = head.left
            
        return root