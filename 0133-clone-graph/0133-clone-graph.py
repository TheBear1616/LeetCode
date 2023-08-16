"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        return self.dfs(node, {})
    
    def dfs(self, node, visited):
        if node.val not in visited:
            newNode = Node(node.val, [])
            visited[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(self.dfs(neighbor, visited))

        return visited[node.val]