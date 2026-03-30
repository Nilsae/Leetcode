# You are given the adjacency list representation of an undirected graph containing nodes labeled 0 to n - 1, where n indicates the number of nodes. Each node's adjacency list will contain the neighboring nodes along with the length of the path to the neighboring nodes. Your task is to implement an algorithm that calculates and returns the number of distinct connected components in the given graph.

# The expected time complexity is 

# O(n+m), where 
# n is the number of vertices and 
# m is the number of edges in the graph.

from typing import List, Tuple

def solution(graph: List[List[Tuple[int, int]]]) -> int:
    num_componenets = 0
    visited = set()
    def explore(node_id):
        if node_id in visited:
            return
        visited.add(node_id)
        for neighbor in graph[node_id]:
            explore(neighbor[0])
    
    
    for node_id in range(len(graph)):
        if node_id not in visited:
            num_componenets += 1
            explore(node_id)
    return num_componenets
                
