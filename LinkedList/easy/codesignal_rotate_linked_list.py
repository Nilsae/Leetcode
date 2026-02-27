# You are given a singly linked list and an integer k. Your task is to write a Python function, rotate_right(linked_list, k), which rotates the linked list to the right by k places. Note that k might be 0 or greater than the length of the linked list.

# Your function should take the last k nodes from the end of the list and move them to the start of the list, maintaining their original order. After the rotation, return the head of the resulting linked list.

# For instance, if the linked list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, after the rotation, it should become 4 -> 5 -> 1 -> 2 -> 3.

# The expected time complexity for your solution is 

# O(n).



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head: ListNode, k: int) -> ListNode:
    n = 0
    h = head
    while h:
        n += 1
        h = h.next
    k = k % n
    if not k:
        return head
    h = head
    i = 0
    while i < n - 1:
        i += 1
        h = h.next
    h.next = head
    i = 0
    h = head
    # j = 0
    while h:
        if i == n - k - 1:
            new_head = h.next
            h.next = None
            return new_head
        i += 1
        h = h.next