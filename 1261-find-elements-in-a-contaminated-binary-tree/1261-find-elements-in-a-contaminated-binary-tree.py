# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = self.populateTree(root, 0)
        self.values = set()
        self.collectValues(self.root)
    
    def populateTree(self, root, val):
        if not root: return None
        
        root.val = val
        root.left = self.populateTree(root.left, (2 * val) + 1)
        root.right = self.populateTree(root.right, (2 * val) + 2)

        return root

    def collectValues(self, root):
        if not root: return
        self.values.add(root.val)
        self.collectValues(root.left)
        self.collectValues(root.right)

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)