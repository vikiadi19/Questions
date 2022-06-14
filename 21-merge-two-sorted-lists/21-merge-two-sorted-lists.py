# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dhead = temp = ListNode()
        p1, p2 = list1, list2
        while p1 != None and p2!= None:
            if p1.val < p2.val:
                temp.next = p1
                p1 = p1.next
            else:
                temp.next = p2
                p2 = p2.next
            temp = temp.next
        
        temp.next = p1 or p2
        
        return dhead.next
        