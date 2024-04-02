# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = collections.deque([root])
        result = []

        while que:
            level = None
            for _ in range(len(que)):
                node = que.popleft()
                level = node
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            result.append(level.val)
        
        return result