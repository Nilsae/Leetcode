# You are given a linked list, and you are required to detect if a cycle exists in the linked list. A linked list is said to contain a cycle if a node's next pointer points back to one of the previous nodes in the list. Given the head of the linked list head, return True if the linked list contains a cycle and False otherwise.

# You need to solve this using 
# O(1) of additional memory.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    
    # O(n) memory:
    # seen = set()
    # h = head
    # while h:
    #     if h in seen:
    #         return True
    #     else:
    #         seen.add(h)
    #     h = h.next
    # return False

    # O(1) memory: Floyd’s Tortoise and Hare algorithm.
    slow = head
    fast = head
    while(slow.next and fast.next and fast.next.next):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False