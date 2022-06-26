# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        
        midpt = self.mid(head)
        right = midpt.next
        midpt.next = None
        rhead = self.reversals(right)
        p1, p2 = head, rhead
        while p1 != None and p2 != None:
            if p1.val == p2.val:
                p1, p2 = p1.next, p2.next
            else:
                return False
        return True
    
                
    
    def mid(self, head):
        slow = fast = head
        while fast.next != None and fast.next.next!= None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reversals(self, head):
        p, c = None, head
        while c is not None:
            nex = c.next
            c.next = p
            p = c
            c = nex
            
        return p            
        
        
        
            
        
        