# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        que = collections.deque([root])

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                leftValFound = False
                if node.left: 
                    if node.left.val in (x, y): leftValFound = True
                    que.append(node.left)
                if node.right: 
                    if node.right.val in (x, y) and leftValFound:
                        return False
                    que.append(node.right)
                level.append(node.val)
            if x in level and y in level:
                return True