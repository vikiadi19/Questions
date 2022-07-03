# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = set()
        def helper(root):
            if root == None:
                return -1
            lh = helper(root.left)
            rh = helper(root.right)
            if not abs(lh-rh)<=1:
                res.add(False)
                
            return max(rh, lh)+1
        
        helper(root)
        if False in res:
            return False
        return True