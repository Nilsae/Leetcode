class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) == 1:
            return edges[0]
        adj_mat = [[0 for i in range(n)] for j in range(n)]
        for edge in edges:
            adj_mat[edge[0]][edge[1]] = 1
            adj_mat[edge[1]][edge[0]] = 1
        centers = [i for i in range(n)]
        last_center = centers
        while(1):
            print(centers)
            leaves = self.removeLeaves(adj_mat, n)
            centers = list(set(centers) - set(leaves))
            if not centers or centers == last_center:
                break
            last_center = centers
        # print(leaves)
        
        print(last_center)
        return last_center
    def removeLeaves(self, adj_mat, n):
        leaves = []
        for node in range(n):
            if sum(adj_mat[node]) == 1:
                leaves.append(node)
        for leaf in leaves:
            for i in range(n):
                adj_mat[i][leaf] = 0
                adj_mat[leaf][i] = 0
        return leaves
Solution().findMinHeightTrees(n=6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]])