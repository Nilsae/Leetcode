# You are provided with two lists of integers, listA and listB. Your task is to determine if listB is a contiguous sublist of listA. You need to return True if listB is a contiguous sublist of listA, and False otherwise.

# A sublist is defined as a subset of consecutive elements within a list. For instance, [2, 3] is a sublist of [1, 2, 3, 4] but not a sublist of [1, 3, 2, 4].

# Note that you are not allowed to use any built-in Python functions for this task except for the len() function to get the length of a list. All other operations should be executed with basic Python programming constructs.

def solution(listA, listB):
    na = len(listA) #big
    nb = len(listB)
    b_left = 0
    for i in range(na - nb + 1):
        i_copy = i
        while listA[i_copy] == listB[b_left]:
            b_left += 1
            i_copy += 1
            if b_left == nb:
                return True
        b_left = 0
    return False