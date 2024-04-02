# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        que = collections.deque([root])
        result = []

        while que:
            level = 0
            qLen = len(que)
            for _ in range(qLen):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                level += node.val
            result.append(level / qLen)
        
        return result