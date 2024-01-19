# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.result = 1e9
        self.preVal = 1e9

        def dfs(node):
            if node:
                dfs(node.left)
                if self.preVal != 1e9:
                    self.result = min(self.result, abs(node.val - self.preVal))
                self.preVal = node.val
                dfs(node.right)
        
        dfs(root)
        return self.result