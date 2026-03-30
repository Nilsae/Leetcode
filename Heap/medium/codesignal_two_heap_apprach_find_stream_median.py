from typing import List
import heapq # only provides a min heap, so to make a max heap, you can push negative values.
def find_stream_median(numbers: List[int]) -> List[float]:
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    left = []
    right = []
    med_stream = []
    for num in numbers:
        if not left or num < -left[0]:
            heapq.heappush(left, -num)
        elif not right or num > right[0]:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)
            
            
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        if len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))
        
        
        if len(left) == len(right):
            med_stream.append(float((-left[0] + right[0]) / 2))
        elif len(left) > len(right):
            med_stream.append(float(-left[0]))
        else:
            med_stream.append(float(right[0]))
    return med_stream




# new implementation:
from typing import List
import heapq
def find_stream_median(numbers: List[int]) -> List[float]:
    right = []
    left = []
    heapq.heappush(right, numbers[0])
    median_arr = [float(numbers[0])]
    for i, num in enumerate(numbers[1:]):
        if num >= right[0]:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)
        if len(left) - len(right) > 1:
            elem = heapq.heappop(left)
            heapq.heappush(right, -elem) #because elem comes from left so it was negated
        if len(right) - len(left) > 1:
            elem = heapq.heappop(right)
            heapq.heappush(left, -elem)
        if len(left) == len(right):
            median_arr.append(float((-left[0] + right[0]) / 2))
        elif len(right) > len(left):
            median_arr.append(float(right[0]))
        else:
            median_arr.append(float(-left[0]))
    return median_arr