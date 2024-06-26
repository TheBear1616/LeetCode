# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def dfs(root):
            if not root: return 

            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        
        dfs(root)

        def convert(low, high):
            if low <= high:
                mid = (low + high) // 2
                node = TreeNode(nums[mid])
                node.left = convert(low, mid - 1)
                node.right = convert(mid + 1, high)

                return node
        
        return convert(0, len(nums) - 1)