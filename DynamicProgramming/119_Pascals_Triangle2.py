class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        rowIndex += 1
        arr = [[1 for j in range(i+1)] for i in range(rowIndex)]
        for i in range(1, rowIndex):
            for j in range(i):
                if j == i:
                    arr[i][j] = arr[i-1][j]
                elif j != 0:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr[-1]
