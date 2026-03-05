# Given a directed acyclic graph (DAG) as an adjacency list, where keys represent nodes and values represent edges from that node to other nodes, implement a function, topological_sort(graph), that performs a topological sort on this graph. The function should return a list containing all the nodes of the graph in topological order.

# If multiple topological orders are possible, the function can return any one of them. If you are unfamiliar, a topological order of a DAG is a linear ordering of its nodes such that for every directed edge u -> v from node u to node v, u comes before v in the ordering.

# For example:

# Python
# Copy to clipboard
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['D'],
#     'D': []
# }

# topological_sort(graph)
# Expected Output: ['A', 'C', 'B', 'D'] or ['A', 'B', 'C', 'D'].

# The expected time complexity is 
# O(n+m), where 
# n is the number of vertices and 
# m is the number of edges in the graph.

from collections import deque
def topological_sort(graph):
    topo = []
    indegrees = {}
    q = deque()
    for node in graph:
        indegrees[node] = 0
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
    
    for node in graph:
        if indegrees[node] == 0:
            q.append(node)
    

    while q:
        node = q.popleft()
        topo.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.append(neighbor)
    return topo