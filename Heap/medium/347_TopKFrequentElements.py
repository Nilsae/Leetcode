from collections import Counter 
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        # dummpy implementation:
        # most_frequent= {}
        # if not nums:
        #     return []
        # most_frequent[-9999999999] = -99999999
        # for num,frequency in counter.items():
        #     if frequency>= min(most_frequent.values()):
        #         if len(most_frequent) == k:
        #             minvalue = min(most_frequent.values())
        #             for key, value in most_frequent.items():
        #                 if value == minvalue:
        #                     most_frequent.pop(key)
        #                     break
        #         most_frequent[num] = frequency
        # return list(most_frequent.keys())

        # heapq ( priority queue algorithm) implementation:
        most_frequent = nlargest(n= k, iterable = counter.items(), key=lambda x: x[1])
        return [i[0] for i in most_frequent]