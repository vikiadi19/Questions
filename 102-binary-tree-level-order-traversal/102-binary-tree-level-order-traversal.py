# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
        ans = []
        q = deque()
        q.append(root)
        while len(q)>0:
            l = len(q)
            ans2 = []
            for i in range(l):
                node = q.popleft()
                ans2.append(node.val)
                if node.left!= None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            ans.append(ans2)
            
        return ans
            
        
                