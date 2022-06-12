# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head
        
        p, c = ListNode(), head
        dhead = p
        while c is not None:
            if c.val == val:
                c = c.next
            else:
                p.next = c
                p = p.next
                c = c.next
                
        p.next = c
        return dhead.next