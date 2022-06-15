# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        slow, fast = head, head.next
        while slow != fast and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if slow ==fast:    
            return True
        return False
    
            
                
            