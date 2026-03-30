# Your task is to write a function that takes a list of strings and an integer k as input. The function should return the k shortest strings in the list in ascending order of their lengths. In the case of ties, prioritize the strings that come earlier in the original list.

# For instance, if the input list is ['cat', 'window', 'defenestrate', 'python', 'algorithm'] and k = 2, the output should be ['cat', 'window'] because they are the two strings with the shortest lengths.

# The solution should work in 
# O
# (
# n
# log
# ⁡
# k
# )
# O(nlogk) time complexity, where n is the number of strings in the list.



from typing import List
import heapq
def find_k_shortest(strings: List[str], k: int) -> List[str]:
    d = {}
    for i, s in enumerate(strings):
        d[s] = i
    l =  heapq.nsmallest(k, d.items(), key = lambda x: (len(x[0]), x[1]))
    ans = []
    for item in l:
        ans.append(item[0])
    return ans


# simpler code:

def find_k_shortest(strings: List[str], k: int) -> List[str]:
    h = heapq.nsmallest(k, enumerate(strings), key = lambda x: (len(x[1]), x[0]))
    return [x[1] for x in h]