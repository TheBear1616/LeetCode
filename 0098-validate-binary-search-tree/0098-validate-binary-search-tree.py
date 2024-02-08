# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right, node):
            if not node:
                return True
            
            return left < node.val < right and dfs(left, node.val, node.left) and dfs(node.val, right, node.right)
        
        return dfs(-math.inf, math.inf, root)