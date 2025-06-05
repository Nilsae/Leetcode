
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited = {}
        return self.dfs(node, visited)
    def dfs(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        
        newNode = Node(val = node.val)
        visited[newNode.val] = newNode
        for adjnode in node.neighbors:
            newNode.neighbors.append(self.dfs(adjnode, visited))
        return newNode