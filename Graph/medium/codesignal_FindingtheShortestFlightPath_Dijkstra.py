# Given the flight map of a city, represented as a dictionary, where the key represents the name of the airport (as a string) and the corresponding value is another dictionary. In the second dictionary, the key represents the name of an airport directly reachable from the first airport, and the corresponding value represents the air distance (in km) between these two airports. Implement Dijkstra’s Algorithm to find the air distance of the shortest path between any two given airports. The function should return the corresponding distance. It is guaranteed the path from start to end always exists.

# For instance:

# graph = {
#     'JFK': {'LAX': 2500, 'MIA': 2000, 'ORD': 1200},
#     'LAX': {'SEA': 2000, 'ORD': 3000},
#     'MIA': {'ORD': 1500, 'ATL': 2000, 'DFW': 1800},
#     'ORD': {'SEA': 2800},
#     'SEA': {},
#     'ATL': {'DFW': 1500},
#     'DFW': {}
# }
# Here, JFK, LAX, MIA, and others are names of airports, and distances are in kilometers (km).



import heapq

def shortest_path(graph, start, end):
    if start == end:
        return 0
    node = start
    heap = []
    distances = {}
    visited = set()
    for node in graph:
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
            
    heapq.heappush(heap, (0, start)) 
    def explore(node):
        for neighbor in graph[node]:
            new_dist = graph[node][neighbor] + distances[node]
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    while heap:
        
        dist, node = heapq.heappop(heap)
        if node == end:
            return distances[end]
        if dist == distances[node]: # we only store the smallest distance for each node in distances[node], but the heap might have the same node with bigger distances. Therefore we need to make sure that the node we just popped from the heap is the one with the smallest distance and only then explore it
            explore(node)
    return distances[end]