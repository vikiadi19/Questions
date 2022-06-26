# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        
        midpt = self.mid(head)
        left = head
        right = midpt.next
        midpt.next = None
        leftL = self.sortList(left)
        rightL = self.sortList(right)
        
        mergeL = self.merge(leftL, rightL)
        return mergeL
    
    def mid(self, head):
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
         
        return slow
    
    
    def merge(self, l, r):
        nnode = nhead = ListNode()
        while l!=None and r!=None:
            if l.val<r.val:
                nnode.next = l
                l = l.next
            else:
                nnode.next = r
                r = r.next
            nnode = nnode.next
        nnode.next = l or r
        
        return nhead.next
        