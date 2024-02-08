# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columnDict = collections.defaultdict(list)
        que = collections.deque([(root, 0)])
        minCol, maxCol = 0, 0

        while que:
            node, column = que.popleft()
            if node:
                columnDict[column].append(node.val)
                minCol = min(minCol, column)
                maxCol = max(maxCol, column)
                que.append((node.left, column - 1))
                que.append((node.right, column + 1))
        
        return [columnDict[col] for col in range(minCol, maxCol + 1)]