# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head and head.next:
            nextPair = head.next.next
            secondNode = head.next
            
            secondNode.next = head
            head.next = nextPair
            prev.next = secondNode
            
            prev = head
            head = head.next
        
        return dummy.next
             