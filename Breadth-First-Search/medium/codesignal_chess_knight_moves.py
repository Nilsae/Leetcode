from collections import deque
def knight_moves(board, start, end):
    """
    Your task is to write a function that calculates the minimum number of moves 
    it would take for a knight to get from `start` to `end` on a chessboard.
    
    :param board: 2D array representing the chess board
    :param start: a tuple (x,y) representing the starting cell on the board
    :param end: a tuple (x,y) representing the end cell on the board

    :return: minimum number of steps required for a knight to reach from start to end
    """

    q = deque()
    q.append(start)
    visited = set()
    num_moves = [[float('inf') for i in range(8)] for j in range(8)]
    num_moves[start[0]][start[1]] = 0
    possible_jumps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    while q:
        node = q.popleft()
        if node not in visited:
            for jump in possible_jumps:
                ni = node[0] + jump[0]
                nj = node[1] + jump[1]
                if ni < 8 and nj < 8 and ni >=0 and nj >=0 and (ni, nj) not in visited:
                    num_moves[ni][nj] = min(num_moves[node[0]][node[1]] + 1, num_moves[ni][nj])
                    q.append((ni, nj))
            visited.add(node)
    return num_moves[end[0]][end[1]]