# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(node):
            if node==None:
                return 0
            nonlocal max_sum
            l_sum = dfs(node.left) 
            r_sum = dfs(node.right)
            l_sum = max(l_sum, 0)
            r_sum = max(r_sum, 0)
            summ = l_sum + r_sum + node.val
            max_sum = max(summ, max_sum)
            return max(l_sum, r_sum) + node.val
            
        dfs(root)
        return max_sum