# You are given a list of n strings of varied lengths. Write a function find_anagrams(strs) that takes this list and returns a list of lists. Each sublist should contain strings that are anagrams of each other, sorted in lexicographical order. The final list of lists should also be sorted lexicographically by the first string in each sublist.

# In this problem, an anagram is defined as a word or phrase that is formed by rearranging the letters of a different word or phrase. For example, the words cinema and iceman are anagrams because they contain the same letters.

# Your solution should have a time complexity of 

# O(n⋅m⋅logm), where n is the number of strings in the list, and m is the maximum length of a string in the list.


from collections import Counter
def find_anagrams(strs):
    seen_counters = {}
    num = 0
    for i in range(len(strs)):
        c = Counter(list(strs[i]))
        t = tuple(sorted(c.items())) # because Counter object (or any dict) is UNHASHABLE
        if t not in seen_counters:
            seen_counters[t] = num
            num += 1
    answer = [[] for i in range(len(seen_counters))]
    for i in range(len(strs)):
        c = Counter(list(strs[i]))
        t = tuple(sorted(c.items()))
        answer[seen_counters[t]].append(strs[i])
    for i in range(len(answer)):
        answer[i] = sorted(answer[i])
    return sorted(answer)