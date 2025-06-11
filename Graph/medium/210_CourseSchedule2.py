class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            ans = [i for i in range(numCourses)]
            ans.reverse()
            return ans
        adj_mat = [[0 for i in range(numCourses)] for j in range(numCourses)]
        for couple in prerequisites:
            adj_mat[couple[1]][couple[0]] = 1
        visited = {i: False for i in range(numCourses)}
        visiting = {i: False for i in range(numCourses)}
        ans = []
        try:
            for course in range(numCourses):
                if not visited[course]:
                    self.DFS(adj_mat, ans, visited,visiting, course)
            ans.reverse()
            return ans
        except:
            return [] 
    def DFS(self,adj_mat ,ans, visited,visiting, course ):
        if visited[course]:
            return course
        if visiting[course]:
            raise Exception("cycle")
        visiting[course] = True
        for idx, adj_course in enumerate(adj_mat[course]):
            if adj_course ==1:
                self.DFS(adj_mat, ans, visited,visiting, course = idx)
        visiting[course] = False
        visited[course] = True
        if course not in ans:
            ans.append(course)
        return
# print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]