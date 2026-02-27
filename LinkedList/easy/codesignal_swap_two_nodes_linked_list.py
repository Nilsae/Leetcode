class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     # Holds the value or data of the node
        self.next = next  # Points to the next node in the linked list; default is None

def swap_linked_list_nodes(head, start, end):
    n = -1
    dummy = ListNode()
    dummy.next = head
    h = dummy
    after_end = None
    before_start = None
    while (h):
        if n == end - 1:
            before_end = h
            end_node = h.next
            after_end = h.next.next
        if n == start - 1:
            before_start = h
            start_node = h.next
            after_start = h.next.next
        n = n + 1
        h = h.next
    before_start.next = end_node
    end_node.next = after_start
    before_end.next = start_node
    start_node.next = after_end
    
    return dummy.next if start == 0 else head
    