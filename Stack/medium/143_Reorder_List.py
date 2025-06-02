# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        dummy = head
        total_elems = 0
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
            total_elems = total_elems+1
        if total_elems ==1:
            return
        while(len(stack)>(total_elems/2)):
            save = head.next
            head.next =stack.pop()
            head = head.next
            head.next = save
            head = head.next
        if total_elems%2:
            save = head.next
            head = head.next
            head.next = save
            head = head.next
        head.next = None

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]