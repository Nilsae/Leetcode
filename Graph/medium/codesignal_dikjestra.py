# Your task is to write a Python function shortest_path(grid, source, destination) that takes a given grid of size 

# n×n, a start cell, and a destination cell and determines the shortest path using Dijkstra’s Algorithm. The function should return the length of the shortest path and the path itself.

# The grid is given as a 2D list of booleans representing the intersections. True means that there is an intersection, and False means that the intersection is blocked. From any intersection, it is possible to move to any directly neighboring intersection (top, bottom, left, or right) if there is a path (True). All paths have the same weight, i.e., 1.

# If the path doesn't exist, return (-1, []).







import heapq
def shortest_path(grid, source, destination):
    n = len(grid)
    # shortest distance from source to every reacheable cell
    distances = [[10000000 for i in range(n)] for j in range(n)]
    distances[source[0]][source[1]] = 0 
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    node = source
    heap = []
    def explore(node):
        neighbors = [(node[0] + dx, node[1] + dy) for dx, dy in moves]
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < n and neighbor[1] >= 0 and neighbor[1] < n and grid[neighbor[0]][neighbor[1]]:
                if distances[node[0]][node[1]] + 1 < distances[neighbor[0]][neighbor[1]]:
                    distances[neighbor[0]][neighbor[1]] = distances[node[0]][node[1]] + 1
                    heapq.heappush(heap, (distances[neighbor[0]][neighbor[1]], neighbor))
    path = [source]
    while node != destination:
        explore(node)
        if not heap:
            return (-1, [])
        _, node = heapq.heappop(heap)
        path.append(node)
        
    return (distances[destination[0]][destination[1]], path)