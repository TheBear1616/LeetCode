# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_gcd(a, b):
            return a if b == 0 else calculate_gcd(b, a % b)

        if not head or not head.next:
            return head
        
        curr = head
        currNext = head.next

        while currNext:
            num1, num2 = curr.val, currNext.val
            gcd = calculate_gcd(num1, num2)
            newNode = ListNode(gcd)
            curr.next = newNode
            newNode.next = currNext
            curr = currNext
            currNext = currNext.next
        
        return head