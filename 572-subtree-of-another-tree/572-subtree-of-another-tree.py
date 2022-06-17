# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None: return False
        if subRoot == None: return True
        
        if root == None:
            return False
        
        
        if self.sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))
    
    
    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        if p.val!=q.val:
            return False
        
        val = self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        return val
        
        