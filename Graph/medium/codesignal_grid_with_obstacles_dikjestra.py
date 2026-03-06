# You are provided with a rectangular grid represented as a matrix, where each cell has an integer. The cells with positive integers represent clear paths that can be passed, and the number in the cell denotes the amount of effort required to pass through that cell. The cells with -1 represent obstacles that cannot be passed.

# Your task is to write a function, find_shortest_path(grid, start, end), where:

# grid is a list of lists where grid[x][y] denotes the property of the cell at row x and column y. The top-left corner of the grid is (0, 0), and the bottom-right corner is (len(grid) - 1, len(grid[0]) - 1).
# start and end are tuples, each having two elements representing the row and column coordinates, respectively.
# If the start cell or the end cell is an obstacle, or if the end cell cannot be reached from the start cell, the function should return -1.


import heapq
def find_shortest_path(grid, start, end):
    if grid[start[0]][start[1]] == -1 or grid[end[0]][end[1]] == -1:
        return -1
    num_rows = len(grid)
    num_cols = len(grid[0])
    node = start
    heap = []
    heapq.heappush(heap, (grid[start[0]][start[1]], start))
    distances = [[float('inf') for i in range(num_cols)] for j in range(num_rows)]
    distances[start[0]][start[1]] = grid[start[0]][start[1]]
    
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def explore(node):
        for move in moves:
            n0 = node[0] + move[0]
            n1 = node[1] + move[1]
            if n0 >=0 and n0 < num_rows and n1 >= 0 and n1 < num_cols and grid[n0][n1] != -1:
                if distances[node[0]][node[1]] + grid[n0][n1] < distances[n0][n1]:
                    distances[n0][n1] = distances[node[0]][node[1]] + grid[n0][n1]
                    heapq.heappush(heap, (distances[n0][n1], (n0, n1)))
                    
    
    
    while heap:
        dist, node = heapq.heappop(heap)
        if node == end:
            return dist
        if distances[node[0]][node[1]] == dist:
            explore(node)
        
    return -1