# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(root):
            if not root:
                return TreeNode(val)

            if val < root.val:
                root.left = dfs(root.left)
            if val > root.val:
                root.right = dfs(root.right)
            
            return root

        return dfs(root)