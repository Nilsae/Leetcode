#  inefficient:
import heapq
# from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        answer = []
        for i in range(k - 1):
            heapq.heappush(h, (i, nums[i]))
        for left in range(k - 1, len(nums)):
            if left != k - 1:   
                heapq.heappop(h)
            heapq.heappush(h, (left, nums[left]))
            m = heapq.nlargest(1, h, key = lambda x: x[1])
            answer.append(m[0][1])
        return answer


# efficient:
from collections import deque
# q[0] (front of deque) is the index of the current maximum element in the window
# q[-1] (back of deque) is the most recently added candidate
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []
        if k == 1:
            return nums
        for i in range(k - 1):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        for right in range(k - 1, len(nums)):
            # print(right, q)
            while q and nums[q[-1]] < nums[right]:
                q.pop() # removes q[-1]
            while q and q[0] < right - k + 1:
                q.popleft() # removes q[0]
            q.append(right)
            answer.append(nums[q[0]])
            
        return answer

