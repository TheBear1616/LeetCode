# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(low, high):
            if low <= high:
                mid = (low + high) // 2
                newNode = TreeNode(nums[mid])
                newNode.left = convert(low, mid-1)
                newNode.right = convert(mid+1, high)
                
                return newNode
        
        return convert(0, len(nums)-1)