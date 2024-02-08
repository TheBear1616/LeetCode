"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = {None: None}
        
        currNode = head
        while currNode:
            nodeDict[currNode] = Node(currNode.val)
            currNode = currNode.next
        
        currNode = head
        while currNode:
            nodeDict[currNode].next = nodeDict[currNode.next]
            nodeDict[currNode].random = nodeDict[currNode.random]
            currNode = currNode.next
        
        return nodeDict[head]