# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    LCA = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        self.LCA = root
        
        def dfs(root):
            if not root:
                return (False, False)

            statusLeft = dfs(root.left)
            statusRight = dfs(root.right)

            status = (True if root.val == p.val else statusLeft[0] or statusRight[0], True if root.val == q.val else statusLeft[1] or statusRight[1])

            if status[0] and status[1]:
                self.LCA = root
                return (False, False)
        
            return status
        
        dfs(root)

        return self.LCA