# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
    #     """
    #     :type list1: Optional[ListNode]
    #     :type list2: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
        res = ListNode()
        head_copy = res
        while( list1 and list2):
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
            
        if list1:
            res.next = list1
        if list2:
            res.next = list2
        # or res.next = list1 or list2
        return head_copy.next
        
    # def messy_mergeTwoLists(self, list1, list2):
    # #     """
    # #     :type list1: Optional[ListNode]
    # #     :type list2: Optional[ListNode]
    # #     :rtype: Optional[ListNode]
    # #     """
    #     res = ListNode()
    #     head_copy = res
    #     while( list1 and list2):
    #         if list1.val==list2.val:
    #             res.next = list1
    #             list1 = list1.next
    #             res = res.next
    #             res.next = list2
    #             list2 = list2.next
    #             res = res.next
    #         elif list1.val<list2.val:
    #             res.next = list1
    #             list1 = list1.next
    #             res = res.next
    #         elif list1.val>list2.val:
    #             res.next = list2
    #             list2 = list2.next
    #             res = res.next
    #     while(list1):
    #         res.next = list1
    #         list1 = list1.next
    #         res = res.next
    #     while(list2):
    #         res.next = list2
    #         list2 = list2.next
    #         res = res.next
    #     return head_copy.next
        
            
Solution().mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]