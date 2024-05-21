"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        self.LCA = None

        def findRoot(node):
            if not node.parent: return node
            return findRoot(node.parent)

        def dfs(root):
            if not root: return (False, False)

            statusLeft = dfs(root.left)
            statusRight = dfs(root.right)

            status = (True if p == root else statusLeft[0] or statusRight[0], True if q == root else statusLeft[1] or statusRight[1])

            if status[0] and status[1]:
                self.LCA = root
                return(False, False)
            
            return status
        
        dfs(findRoot(p))

        return self.LCA