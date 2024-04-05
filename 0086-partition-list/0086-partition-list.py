# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = lessCurr = ListNode(16)
        tempHead = moreCurr = ListNode(16)

        while head:
            if head.val < x:
                lessCurr.next = ListNode(head.val)
                lessCurr = lessCurr.next
            else:
                moreCurr.next = ListNode(head.val)
                moreCurr = moreCurr.next
            head = head.next

        lessCurr.next = tempHead.next 
        
        return result.next
        