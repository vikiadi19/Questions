# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class DiaPair:
    def __init__(self, ht = -1, dia = 0):
        self.ht = ht
        self.dia = dia
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dia(root):
            if root == None:
                bp = DiaPair()
                return bp

            lp = dia(root.left)
            rp = dia(root.right)

            mp = DiaPair()
            mp.ht = max(lp.ht, rp.ht)+1
            mp.dia = max((lp.ht+rp.ht+2), lp.dia, rp.dia)

            return mp
        
        res = dia(root)
        return res.dia
    
        