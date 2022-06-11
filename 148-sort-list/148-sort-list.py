# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        left = head
        right = self.mid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        merge_both = self.merge(left, right)
        
        return merge_both
    
    def mid(self, node):
        slow, fast = node, node
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge(self, left, right):
        n = dhead = ListNode()
        while left != None and right != None:
            if left.val<right.val:
                n.next = left
                left = left.next
            else:
                n.next = right
                right = right.next
            n = n.next
        n.next = left or right
        
        return dhead.next
    
        