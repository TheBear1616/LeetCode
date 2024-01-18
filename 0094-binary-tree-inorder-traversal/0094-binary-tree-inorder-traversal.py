# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        def inOrder(node):
            if node:
                inOrder(node.left)
                result.append(node.val)
                inOrder(node.right)
        
        inOrder(root)
        return result
