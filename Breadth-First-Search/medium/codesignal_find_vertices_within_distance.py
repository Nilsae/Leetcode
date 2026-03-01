# You are given a graph represented as an adjacency list and a starting vertex, start. The graph is undirected and could be either connected or not connected. The vertices are labeled with unique positive integers starting from 1. The task is to implement a function, find_vertices_within_distance(graph, start, distance), that returns a list of all vertices, sorted in ascending order by their numbers, whose distance is less than or equal to distance from the starting vertex. The distance is defined as the minimum number of edges traversed to get from one vertex to another.

# Here is how the graph would be represented in Python:

# graph = {
#     1: [2, 3],
#     2: [1, 4, 5],
#     3: [1],
#     4: [2],
#     5: [2, 6],
#     6: [5]
# }
# Vertices 2 and 3 are adjacent to vertex 1. Vertices 1, 4, and 5 are adjacent to vertex 2, and so on. For example, if start = 1 and distance = 2, your function should return [1, 2, 3, 4, 5].

# The expected time complexity is 
# O(n), where 
# n is the number of vertices in the graph.




from collections import deque
def find_vertices_within_distance(graph, start, distance):
    q = deque([start])
    distances = {}
    visited = set()
    distances[start] = 0
    while q:
        node = q.popleft()
        if node not in visited:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if neighbor in distances:
                        distances[neighbor] = min(distances[neighbor], distances[node] + 1) 
                    else:
                        distances[neighbor] = distances[node] + 1
                if neighbor in graph:
                    q.extend([neighbor])
            visited.add(node)
    ans = []
    for n, d in distances.items():
        if d <= distance:
            ans.append(n)
    return sorted(ans)
    
        