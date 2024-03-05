# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = collections.deque([root])
        result = []
        ltor = True

        while len(que) > 0:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                level.append(node.val)

            result.append(level if ltor else level[::-1])
            ltor = not ltor
        
        return result