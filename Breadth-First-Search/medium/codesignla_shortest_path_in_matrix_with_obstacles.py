# You are provided with a matrix of 

# n×m elements (0s and 1s). You can interpret 1 as a passable cell and 0 as an obstacle. You need to implement a function bfs_matrix(matrix, start, end), which returns the length of the shortest path from the start point to the end. The start and end points are tuples (int, int) indicating the matrix cell (e.g., (0, 0) for the top-left). If the path is impossible, return 0. It is guaranteed the starting point always contains 1 in the matrix, i.e. there is no obstacle there.

# Note: You can only move vertically or horizontally; diagonal movement is forbidden.

# The expected time complexity for the problem is 
# O(n⋅m).


from collections import deque
def bfs_matrix(mat, start, end):
    q = deque([start])
    visited = set()
    num_rows = len(mat)
    num_cols = len(mat[0])
    path_length = [[float('inf') for j in range(num_cols)] for i in range(num_rows)]
    path_length[start[0]][start[1]] = 0
    while q:
        node = q.popleft()
        if node not in visited:
            cur_path_len = path_length[node[0]][node[1]]
            if node[1] + 1 < num_cols and mat[node[0]][node[1] + 1] == 1:
                path_length[node[0]][node[1] + 1] = min(path_length[node[0]][node[1] + 1], cur_path_len + 1)
                q.append((node[0], node[1] + 1))
            if node[1] - 1 >= 0  and mat[node[0]][node[1] - 1] == 1:
                path_length[node[0]][node[1] - 1] = min(path_length[node[0]][node[1] - 1], cur_path_len + 1)
                q.append((node[0], node[1] - 1))
            if node[0] + 1 < num_rows and mat[node[0] + 1][node[1]] == 1:
                path_length[node[0] + 1][node[1]] = min(path_length[node[0] + 1][node[1]], cur_path_len + 1)
                q.append((node[0] + 1, node[1]))
            if node[0] - 1 >= 0 and mat[node[0] - 1][node[1]] == 1:
                path_length[node[0] - 1][node[1]] = min(path_length[node[0] - 1][node[1]], cur_path_len + 1)
                q.append((node[0] - 1, node[1]))
            visited.add(node)
    if path_length[end[0]][end[1]] == float('inf'):
        return 0
    return path_length[end[0]][end[1]] 
    
            