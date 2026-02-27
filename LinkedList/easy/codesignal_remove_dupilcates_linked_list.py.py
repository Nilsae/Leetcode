# Your task is to write a function, remove_duplicates(head). This function takes the head of a linked list as a parameter. The function should remove all duplicate nodes from an unsorted linked list and return the head of the updated linked list. The order of the remaining nodes in the list should be the same as in the original.

# In other words, if a linked list has duplicate values, all occurrences of such values, except for their first occurrence, must be deleted from the list. For instance, for the given linked list 1 -> 3 -> 2 -> 3 -> 2 -> 3 -> 4 -> 5 -> 5 -> 5 you should return 1 -> 3 -> 2 -> 4 -> 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    h = head
    seen = set()
    prev = h
    while(h):
        if h.val in seen:
            prev.next = h.next
        else:
            seen.add(h.val)
            prev = h
        h = h.next
    return head