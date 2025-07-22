from collections import deque # more efficient than q = [] , q.pop(0) - (O(n) vs O)

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        adj_mat = [[0 for i in range(numCourses)] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_mat[course][prereq] = 1
        num_incoming = {i:sum(row[i] for row in adj_mat) for i in range(numCourses)}
        q = deque()
        sorted_list = []
        to_delete = []
        for c, num_incoming_val in num_incoming.items():
            if num_incoming_val == 0:
                q.append(c)
                to_delete.append(c)
        for key in to_delete:
            num_incoming.pop(key)
        to_delete = []
        while q:
            node = q.popleft()
            sorted_list.append(node)
            for idx, adj in enumerate(adj_mat[node]):
                if adj and idx in num_incoming:
                    num_incoming[idx] -= 1
                    if num_incoming[idx] ==0:
                        q.append(idx)
                        to_delete.append(idx)
            for key in to_delete:
                num_incoming.pop(key)
            to_delete = []
        if len(sorted_list) == numCourses:
            return True
        return False