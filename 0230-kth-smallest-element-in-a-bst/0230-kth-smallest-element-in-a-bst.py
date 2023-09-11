# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        
        def dfs(root):
            if root:
                heapq.heappush(minHeap, root.val * -1)
                if len(minHeap) > k:
                    heapq.heappop(minHeap)
                if root.left: dfs(root.left)
                if root.right: dfs(root.right)
        
        dfs(root)
        return minHeap[0] * -1