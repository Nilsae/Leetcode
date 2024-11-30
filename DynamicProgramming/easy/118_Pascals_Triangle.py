class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = [[1 for j in range(i+1)] for i in range(numRows)]
        print(arr)
        for i in range(1, numRows):
            for j in range(i):
                print(i)
                print(j)
                if j == i:
                    arr[i][j] = arr[i-1][j]
                elif j != 0:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(i)
            print(j)
            print(arr)
        return arr

Solution().generate(4)