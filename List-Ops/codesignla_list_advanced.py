
# You are provided with two input lists that contain n and m integers, respectively. Both lists are sorted in non-decreasing order — i.e., every element is either equal to or larger than the preceding one.

# Your task is to return a new list that results from merging the two input lists so that the final output list is also in non-decreasing order. It should contain all the elements of the two lists, maintaining their order within the lists.

# Your solution should not use the built-in sort function of Python but should instead use a technique similar to the one used in the lesson. The expected time complexity is 

# O(n+m).

def solution(l1, l2):
    idx1 = 0
    idx2 = 0
    ans = []
    while(idx1 < len(l1) and idx2 < len(l2)):
        if l1[idx1] < l2[idx2]:
            ans.append(l1[idx1])
            idx1 += 1
        elif l1[idx1] > l2[idx2]:
            ans.append(l2[idx2])
            idx2 += 1
        else:
            ans.append(l1[idx1])
            ans.append(l2[idx2])
            idx1 += 1
            idx2 += 1
    while idx1 < len(l1):
        ans.append(l1[idx1])
        idx1 += 1
    while idx2 < len(l2):
        ans.append(l2[idx2])
        idx2 += 1
    return ans




# You work with large data sets in Python, and typically, the data arrive sorted within individual batches but not across all batches. You are given n lists, where each list is sorted in ascending order. The function should return a single list consisting of all elements from all lists, sorted in ascending order.

# The time complexity of your solution should be 

# O(n⋅m), where n is the total number of lists and m is the maximum length of any list.

# Your solution is not allowed to use built-in functions like sorted, sort, or additional libraries like heapq.
def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    indices = [0 for i in range(len(arr))]
    ans = []
    finished_lists = set()
    candidiates = []
    for i in range(len(indices)):
        if arr[i]:
            candidiates.append(arr[i][0])
    just_merged = min(candidiates)
    while(len(finished_lists) < len(arr)):
        for i in range(len(arr)):
            if i not in finished_lists and indices[i] < len(arr[i]) and arr[i][indices[i]] == just_merged:
                ans.append(just_merged)
                indices[i]  = indices[i] + 1
                if indices[i] == len(arr[i]):
                    finished_lists.add(i)
        candidiates = []
        for i in range(len(indices)):
            if i not in finished_lists and indices[i] < len(arr[i]):
                candidiates.append(arr[i][indices[i]])
        if not candidiates:
            break
        just_merged = min(candidiates)
    
    return ans
    
    
