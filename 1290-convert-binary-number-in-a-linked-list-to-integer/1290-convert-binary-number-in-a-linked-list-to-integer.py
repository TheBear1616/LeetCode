# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = []
        result = 0
        
        while head:
            num.append(head.val)
            head = head.next
        
        idx = 0
        for i in range(len(num)-1, -1, -1):
            result += (num[i] * (2** idx))
            idx += 1
        
        return result