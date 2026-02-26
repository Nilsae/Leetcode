# You are given a square matrix of n x n size. Your task is to write a Python function that indicates whether the matrix is a Toeplitz matrix.

# In a Toeplitz matrix, each descending diagonal (from left to right) is constant. That is, elements in each descending diagonal are the exact same.

# For example, if the given matrix is:

# Plain text
# Copy to clipboard
# 6 7 8
# 4 6 7
# 1 4 6
# Your function should return True because all diagonals that run from the top-left to the bottom-right (↘ direction) are constant:

# [1], [4, 4], [6, 6, 6], [7, 7], [8]
# (Each of these diagonals goes from upper-left towards lower-right.)


from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   # 0 1 2
   # 1
   # 2
   # [[],
   #  [],
   #  []]
   ncol = len(matrix[0])
   nrow = len(matrix)
   #diagonal and above diagonal
   for i_c in range(nrow):
      j = 0
      i = i_c
      elem = matrix[i][j]
      while( (j < ncol ) and (i < nrow)):
         if  matrix[i][j] != elem:
            return False
         i += 1
         j += 1
   
   # below diagonal:
   for j_c in range(1, nrow):
      j = j_c
      i = 0
      elem = matrix[i][j]
      while( (j < ncol ) and (i < nrow )):
         if matrix[i][j] != elem:
            return False
         i += 1
         j += 1
          
   return True