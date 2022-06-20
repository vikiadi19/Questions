# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        summ = [0]
        
        def tilt(root):
            if root == None:
                return 0
            ls = tilt(root.left)
            rs = tilt(root.right)
            summ[0] += abs(rs-ls)
            return ls+rs+root.val
        
        tilt(root)
        
        return summ[0]