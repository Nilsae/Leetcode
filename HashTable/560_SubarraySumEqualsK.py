class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ans = 0

        h = {} # store the complements
        s = 0
        prefix = [0 for i in range(l)]
        for i in range(l):
            s += nums[i]
            prefix[i] = s
            

            if s - k in h:
                ans += h[s - k]
            if s == k:
                ans += 1
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        return ans
#  curr - prev = k
# -prev = k - curr
# prev = curr - k