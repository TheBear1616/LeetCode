# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return root
        
        self.result = ''

        def preOrder(node):
            if node:
                self.result += '(' 
                self.result += str(node.val)
                if not node.left and node.right:
                    self.result += '()'
                preOrder(node.left)
                preOrder(node.right)
                self.result += ')'

        preOrder(root)
    
        return self.result[1:-1]