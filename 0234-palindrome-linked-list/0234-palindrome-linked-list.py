# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        count = 0

        while fast and fast.next:
            count += 1
            slow = slow.next
            fast = fast.next.next

        slo = slow.next if count%2 == 1 else slow

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        
        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        
        return True

        