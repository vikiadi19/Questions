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
        if head is None:
            return None
        
        midpt = self.mid(head)
        right = midpt.next
        midpt.next = None
        # left = head
        rhead = self.reverse(right)
        p1, p2 = head, rhead
        dhead = p3 = ListNode()
        while p1!= None and p2!= None:
            p3.next = p1
            p3 = p3.next
            p1 = p1.next
            p3.next = p2
            p3 = p3.next
            
            p2 = p2.next
            
        p3.next = p1 or p2
            
        return dhead.next
    
    def mid(self, head):
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    
    def reverse(self, head):
        p, c = None, head
        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n
            
        return p