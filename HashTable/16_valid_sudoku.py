
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                rows[row].add(val)
                if val in columns[col]:
                    return False
                columns[col].add(val)
                box_indx = (row //3) * 3 + col//3
                if val in boxes[box_indx]:
                    return False
                boxes[box_indx].add(val)
        return True
    
print(Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


 0  1  2  3  4  5  6  7
 8  9  10 11 12 13 14 15
 16 17 18 19 20 21 22 23
 
 (0, 0)
 (0, 1)
 (0, 2)
 (1, 0)  ->  0
 (1, 1)
 (1, 2)
 (2, 0)
 (2, 1)
 (2, 2)
 
 (0, 3)
 (0, 4)
 (0, 5)
 (1, 3)  -> 1
 (1, 4)
 (1, 5)
 (2, 3)
 (2, 4)
 (2, 5)