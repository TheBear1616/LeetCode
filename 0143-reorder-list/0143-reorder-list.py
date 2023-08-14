# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second
            second = second.next
            temp.next = prev
            prev = temp

        first, second = head, prev

        while second:
            slow, fast = first.next, second.next
            first.next = second
            second.next = slow
            first, second = slow, fast