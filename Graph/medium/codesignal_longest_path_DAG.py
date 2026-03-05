# You are given a Directed Acyclic Graph (DAG) with n vertices and m edges. Each edge has an associated weight. Your task is to implement an algorithm that finds the longest path in the graph. A path is a series of vertices in a graph such that each vertex is connected to the next vertex by an edge.

# The DAG is represented as an adjacency list using 0-based indexing. Specifically, graph is a list of n elements where graph[i] contains a list of tuples (neighbor, weight), representing a directed edge from vertex i to vertex neighbor with the given weight.

# Your solution should have a time complexity of 

# O(n⋅(n+m)).


from collections import deque
def longest_path(graph, num_vertices):
    # print(graph)
    q = deque()
    topo = []
    indegrees = {}
    # we should do topological sorting to see which node comes before which
    # later - after toposort  is complete -  we keep track of the largest path to each node
    for node in range(num_vertices):
        indegrees[node] = 0
    for node in range(num_vertices):
        for t in graph[node]:
            indegrees[t[0]] += 1
                
    for node in range(num_vertices):
        if indegrees[node] == 0:
            q.append(node)
    
    
    while q:
        node = q.popleft()
        topo.append(node)
        for t in graph[node]:
            indegrees[t[0]] -= 1
            if indegrees[t[0]] == 0:
                q.append(t[0])
    
    # now on to finding the largest path
    largest_distances = {}
    for i in range(num_vertices):
        largest_distances[i] = 0
 
    for node in topo:
        for t in graph[node]:
            if t[1] + largest_distances[node] > largest_distances[t[0]]:
                largest_distances[t[0]] = t[1] + largest_distances[node]
    
    return largest_distances[topo[-1]]