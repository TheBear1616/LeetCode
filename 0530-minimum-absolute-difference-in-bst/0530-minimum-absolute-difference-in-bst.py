# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = 1e9
        self.prevValue = None

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            if self.prevValue is not None: 
                self.minDiff = min(self.minDiff, root.val - self.prevValue)
            self.prevValue = root.val
            inOrder(root.right)

        inOrder(root)
        return self.minDiff