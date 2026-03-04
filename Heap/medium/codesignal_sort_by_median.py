import heapq
import statistics

# simple 
# def sort_by_median(nums):
#     med = statistics.median(nums)
#     return heapq.nsmallest(len(nums), nums, key = lambda x: (abs(x - med), x))




# using heapq all the way
# When you push a tuple into a heap, it sorts by the first element of the tuple. If there’s a tie, it uses the second element, and so on. 
def sort_by_median(nums):
    med = statistics.median(nums)
    heap = []
    for num in nums:
        heapq.heappush(heap, (abs(num - med), num))

    s = []
    while heap:
        s.append(heapq.heappop(heap)[1])
    return s
