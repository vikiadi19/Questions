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
        midpt = self.mid(head)
        rhead = midpt.next
        midpt.next = None
        
        head and rhead
        rvhead = self.reverse(rhead)
        head and rvhead
        p1, p2 = head, rvhead
        newhead = temp = ListNode()
        while p1!=None and p2!=None:
            temp.next = p1
            temp = temp.next
            p1 = p1.next
            temp.next = p2
            temp = temp.next
            p2 = p2.next
            
        temp.next = p1 or p2
        
        return newhead.next
    
    def reverse(self, node):
        p, c = None, node
        while c!=None:
            n = c.next
            c.next = p
            p = c
            c = n
            
        return p
    
    def mid(self, head):
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            
        return slow