from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        result = []
        que = deque([root])

        while len(que) > 0:
            level = []
            
            for _ in range(len(que)):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                level.append(node.val)
            
            result.append(sum(level)/len(level))
        
        return result