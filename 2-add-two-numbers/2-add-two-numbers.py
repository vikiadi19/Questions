# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head_node = ListNode(-1)
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        l3 = p3 = ListNode()
        p1, p2 = l1, l2
        while p1!=None and p2!=None:
            summ = p1.val + p2.val + carry
            p3.next = ListNode(summ%10)
            carry = summ//10
            p3 = p3.next
            p1, p2 = p1.next, p2.next
            
        while p1!= None:
            summ = p1.val+carry
            p3.next = ListNode(summ%10)
            carry = (summ)//10
            p3 = p3.next
            p1 = p1.next
            
        while p2!= None:
            summ = p2.val + carry
            p3.next = ListNode(summ%10)
            carry = (summ)//10
            p3 = p3.next
            p2 = p2.next
            
        if carry == 1:
            p3.next = ListNode(1)
            
        return l3.next
            
        
        
        
        
        
        
        
        
#         print(sum_node.val)
#         # p1 = l1
#         # p2 = l2
#         while l1 != None and l2 != None:
#             sum_val = l1.val + l2.val
#             if sum_val > 9:
#                 stg = str(sum_val)
#                 val = int(stg[1])
#                 carry = int(stg[0])
#                 sum_node.val = val
#                 sum_node = sum_node.next
#                 sum_node.val = carry
#             else:
#                 sum_node.val = sum_val
#             sum_node = sum_node.next
#             l1 = l1.next
#             l2 = l2.next
        
#         while l2 != None:
#             sum_node.val += l2.val
#             if sum_node.val > 9:
#                 carry = sum_val//10
#                 sum_val = sum_val%10
#                 sum_node.val = sum_val
#                 sum_node.next.val += carry
#             sum_node = sum_node.next
#             l2 = l2.next
            
#         while l1 !=None:
#             sum_node.val += l1.val
#             if sum_node.val > 9:
#                 carry = sum_val//10
#                 sum_val = sum_val%10
#                 sum_node.val = sum_val
#                 sum_node.next.val += carry
#             sum_node = sum_node.next
#             l1 = l1.next
            
#         if sum_node.next == None:
#             if sum_node.val > 9:
#                 carry = ListNode()
#                 carry.val = sum_val//10
#                 sum_node.next = carry
#                 sum_node.val = sum_node%10
                
#         return sum_node.next
                
            
            
            
# carry = sum_val//10
#                 sum_val = sum_val%10
#             sum_node.val = sum_val
#             sum_node.next.val = carry
#             sum_node = sum_node.next
#         while p1 !=None:
#             sum_node.val += p1.val
#             if sum_node.val > 9:
#                 carry = sum_val//10
#                 sum_val = sum_val%10
#             sum_node.val = sum_val
#             sum_node.next.val += carry
#             sum_node = sum_node.next
                
#         while p2 !=None:
#             sum_node.val += p2.val
#             if sum_node.val > 9:
#                 carry = sum_val//10
#                 sum_val = sum_val%10
#             sum_node.val = sum_val
#             sum_node.next.val += carry
#             sum_node = sum_node.next
            
#         