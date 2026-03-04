# You are given an array of n integers where some integers are repeated. Write a function in Python that takes this array and an integer k as inputs. The function needs to return the k most frequent elements from the array in descending order of their frequency. If two numbers have the same frequency, return them in the ascending order. You should optimize your solution by leveraging Python's built-in heapq module.

# The expected time complexity of the solution should be 

# O(nlogk).



import heapq
from collections import Counter
def solution(nums, k):
    c = Counter(nums).items()
    ans = []
    largest_frequencies = heapq.nlargest(k, c, key=lambda x: (x[1], -x[0])) # sort by values(frequencies) desc, if tie, sort by keys (numbers) ascending - because in nlargest the default is descending

    for i in largest_frequencies:
        ans.append(i[0])
 
    return ans