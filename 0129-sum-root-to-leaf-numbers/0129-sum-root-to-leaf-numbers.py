# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = [0]
        self.nums = []
        def dfs(node):
            if not node:
                return
            
            self.nums.append(node.val)
            if not node.left and not node.right:
                self.result.append(int(''.join(map(str, self.nums))))

            if node.left: 
                dfs(node.left)
                self.nums.pop()
            if node.right: 
                dfs(node.right)
                self.nums.pop()

        dfs(root)
        return sum(self.result)