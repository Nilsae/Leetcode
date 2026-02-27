class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    h = head
    n = 0
    val_list = []
    while(h):
        n += 1
        val_list.append(h.val)
        h = h.next
    for i in range(n//2):
        if val_list[i] != val_list[n - i - 1]:
            return False
    return True
        