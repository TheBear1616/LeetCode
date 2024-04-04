# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.treeArray = []
        self.currIdx = 0
        
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            self.treeArray.append(root.val)
            inOrder(root.right)
        
        inOrder(root)

    def next(self) -> int:
        value = self.treeArray[self.currIdx]
        self.currIdx += 1

        return value

        

    def hasNext(self) -> bool:
        return self.currIdx < len(self.treeArray)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()