# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        listLength = 1
        while temp.next:
            listLength += 1
            temp = temp.next
        
        k = k % listLength
        if k == 0:
            return head

        fast = head
        for i in range(listLength - k - 1):
            fast = fast.next
        
        temp.next = head
        head = fast.next
        fast.next = None

        return head