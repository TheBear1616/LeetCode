# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            if len(minHeap) < k:
                heapq.heappush(minHeap, node.val)
            else:
                return minHeap[-1]
            dfs(node.right)
        
        dfs(root)

        return minHeap[-1]