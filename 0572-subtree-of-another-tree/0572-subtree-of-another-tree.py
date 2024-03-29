# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        def sameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            elif not tree1 or not tree2:
                return False
            
            return tree1.val == tree2.val and sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)
        
        return True if sameTree(root, subRoot) else self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)