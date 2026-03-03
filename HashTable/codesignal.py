# You are given two unsorted arrays, array a and array b of integers. Your task is to find the number of pairs from both arrays whose sum is equal to a given number num.

# The expected time complexity for the task is 

# O(len(a)+len(b)).

# O(m.n) ini worst case:
# from collections import Counter
# def sum_pairs(a, b, num):
#     ans = 0
#     j = 0
#     i = 0
#     a = sorted(a)
#     b = sorted(b)
#     dict_a = Counter(a)
#     dict_b = Counter(b)
#     while i < len(a) and j < len(b):
#         if a[i] + b[j] == num:
#             ans += dict_a[a[i]] * dict_b[b[j]]
#             while i < len(a) - 1 and a[i+1] == a[i]:
#                 i += 1
#             while j < len(b) - 1 and b[j+1] == b[j]:
#                 j += 1
#             i = 0
#             j += 1
#         else:   
#             i += 1
#         if i == len(a) and j < len(b):
#                 i = 0
#                 j += 1
    
#     return ans





# efficient O(n+m)
from collections import Counter
def sum_pairs(a, b, num):
    ans = 0

    c = Counter(a)
    for j in range(len(b)):
        if num - b[j] in c:
            ans += c[num - b[j]]
    
    return ans


