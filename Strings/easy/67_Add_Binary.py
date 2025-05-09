class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)> len(b):
            big = a
            small = b
        else:
            small = a
            big = b
        bigger_len = len(big)
        smaller_len = len(small)
        res = []
        cnt = 0
        dif = bigger_len - smaller_len
        for big_idx in range(bigger_len-1, -1, -1):
            small_idx = big_idx - dif
            if small_idx < 0:
                small_val = 0
            else: 
                small_val = int(small[small_idx])
            idx_sum = int(big[big_idx]) + small_val + cnt
            res.append(str(idx_sum % 2))
            cnt = idx_sum // 2
            # if idx_sum ==3:
            #     res.append("1")
            #     cnt = 1
            # if idx_sum ==2:
            #     res.append("0")
            #     cnt = 1
            # elif idx_sum == 1:
            #     res.append("1")
            #     cnt = 0
            # elif idx_sum == 0:
            #     res.append("0")
            #     cnt = 0
        if cnt == 1:
            res.append("1")
        res.reverse()
        return ''.join(res)

Solution().addBinary(a = "1111", b = "1111")
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"


# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
