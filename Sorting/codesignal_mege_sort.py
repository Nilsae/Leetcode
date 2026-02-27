
def merge(l1, l2):
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

def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    if n == 0:
        return []
    mid = n // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
    