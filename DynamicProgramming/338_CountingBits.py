class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        arr = [ 0 for _ in range(n+1)]
        arr[0] = 0
        i=0
        for num in range(1, n+1):
            if num == pow(2, i):
                arr[num] = 1
                i += 1
            elif num > pow(2, i):
                arr[num] = arr[int(num - pow(2, i))] + 1
            else:
                arr[num] = arr[int(num - pow(2, i-1))] + arr[int(pow(2, i-1))]
        return arr
    
# print(Solution().countBits(8))



# efficient:
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize an array to store the number of 1 bits for all numbers up to n
        arr = [0] * (n + 1)

        # Iterate over all numbers from 1 to n
        for i in range(1, n + 1):
            # The number of 1 bits in i is the number of 1 bits in i // 2 plus the least significant bit
            arr[i] = arr[i >> 1] + (i & 1)
        
        return arr
