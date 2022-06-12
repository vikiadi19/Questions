# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        midpoint = self.mid(head)
        mid_next = midpoint.next
        midpoint.next = None
        rhead = self.reverseList(mid_next)
        node = dhead = ListNode()
        p1, p2 = head, rhead
        while p1 != None and p2 != None:
            node.next = p1
            node = node.next
            p1 = p1.next
            node.next = p2
            node = node.next
            p2 = p2.next
        node.next = p1 or p2
            
        return dhead.next
        
    
    def mid(self, head):
        p1, p2 = head, head
        while p2.next != None and p2.next.next !=None:
            p1 = p1.next
            p2 = p2.next.next
        
        return p1
    
    def reverseList(self, head):
        p, c = None, head
        size = 0
        while c is not None:
            
            size += 1
            n = c.next
            c.next = p
            p = c
            c = n
            
        return p
            
        
        