# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstNode = secondNode = curr = head

        while k > 1:
            curr = curr.next
            firstNode = curr
            k -= 1
        
        while curr.next:
            secondNode = secondNode.next
            curr = curr.next
        
        firstNode.val, secondNode.val = secondNode.val, firstNode.val

        return head