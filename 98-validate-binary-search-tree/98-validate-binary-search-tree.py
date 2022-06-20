# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, left, right):
            if node == None:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            
            lt = helper(node.left, left, node.val)
            rt = helper(node.right, node.val, right)
            
            return lt and rt
            
            
        return helper(root, -math.inf, math.inf)
        
        
            
        