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





# new implementation:
from collections import deque
def topological_sort(graph):
    q = deque()
    incoming_edges = {node : 0 for node in graph.keys()}
    for node in graph:
        for neighbor in graph[node]:
            incoming_edges[neighbor] += 1

    q.extend([node[0] for node in incoming_edges.items() if node[1] == 0])
    path = []
    while q:
        node_to_be_del = q.pop()
        path.append(node_to_be_del)
        for node in graph[node_to_be_del]:
            incoming_edges[node] -= 1
            if incoming_edges[node] == 0:
                q.append(node)
   
    return path       


# q.pop() removes and returns the rightmost element (like a stack), while q.popleft() removes and returns the leftmost element (like a queue).

# Use q.popleft() if you want FIFO (first-in, first-out) behavior.
# Use q.pop() if you want LIFO (last-in, first-out) behavior.

# Both pop() and popleft() will work for this problem because any valid topological order is acceptable, and the order you process nodes from the queue just changes which valid order you get.