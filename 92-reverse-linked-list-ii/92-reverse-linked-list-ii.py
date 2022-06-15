# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reversal(l_node):
            p, c = None, l_node
            while c != p2:
                n = c.next
                c.next = p
                p = c
                c = n

            return p
        
        if left == 1:
            p1 = None
            l_node = head
        else:
            p1 = head
            for i in range(1, left-1):
                p1 = p1.next
            l_node = p1.next
        
        
        p2 = head
        for i in range(1, right):
            p2 = p2.next
            #right node, till here reverse
        r_node = p2
        #p2 node after right
        p2 = p2.next
        # print(p2.val)
        
        rhead = reversal(l_node)
        
        if p1 != None and p2 != None:
            p1.next = rhead
            l_node.next = p2
        elif p1 == None and p2 != None:
            l_node.next = p2
            head = rhead
        elif p2 == None and p1 != None:
            p1.next = rhead
        else:
            return rhead
        
        return head
        
        
        # np = l_node
    
        
        
        
        
        
                
        