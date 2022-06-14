# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return
        
        p1, p2 = ListNode(), head
        dhead = p1
        p1.next = head
        for i in range(1, n):
            p2 = p2.next
            
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next
        
        return dhead.next
            
        
            