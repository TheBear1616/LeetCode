# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        slow = fast = head
        prevSlow = None

        while left > 1:
            prevSlow = slow
            slow = slow.next
            left -= 1

        while right > 1:
            fast = fast.next
            right -= 1
        
        prev = fast.next
        fast.next = None

        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        
        if prevSlow:
            prevSlow.next = prev
            return head
        else:
            return prev