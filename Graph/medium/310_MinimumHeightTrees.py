class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n == 1:
            return [0]
        from collections import defaultdict, deque
        edges_map = defaultdict(set)
        for node1, node2 in edges:
            edges_map[node1].add(node2)
            edges_map[node2].add(node1)
        leaves = [node for node in edges_map if len(edges_map[node]) == 1]
        remaining_nodes = n
        while(remaining_nodes>2):
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = edges_map[leaf].pop()
                edges_map[neighbor].remove(leaf)
                if len(edges_map[neighbor]) == 1:
                    new_leaves.append(neighbor)
                del edges_map[leaf]
            leaves = new_leaves
        return leaves
Solution().findMinHeightTrees(n=6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]])