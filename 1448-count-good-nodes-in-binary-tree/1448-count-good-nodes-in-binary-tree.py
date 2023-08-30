# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        if not root:
            return self.count
        
        def dfs(root, value):
            if not root:
                return
            
            if root.val >= value:
                self.count += 1
                value = root.val
            
            dfs(root.left, value)
            dfs(root.right, value)

        dfs(root, root.val)
        return self.count