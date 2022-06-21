# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (subRoot == None):
            return True
        if root == None:
            return False
        
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot) == True:
                return True
        
        x = self.isSubtree(root.left, subRoot)
        y = self.isSubtree(root.right, subRoot)
        
        return x or y
        
        
        
    def sameTree(self, p, q):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        lt = self.sameTree(p.left, q.left)
        rt = self.sameTree(p.right, q.right)
        return lt and rt
        