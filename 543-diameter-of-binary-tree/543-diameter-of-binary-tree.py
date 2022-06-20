# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if root == None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right + 2
            res[0] = max(res[0], diameter)
            height = max(left, right)+ 1
            
            return height
        
        dfs(root)
        return res[0]
        