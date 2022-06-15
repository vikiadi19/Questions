# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        p = head
        hashset = set()
        while p != None:
            if p in hashset:
                return True
            else:
                hashset.add(p)
            p = p.next
        return False
    
            
                
            