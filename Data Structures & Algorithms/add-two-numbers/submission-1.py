# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1,None)
        curr = sentinel
        carry = 0
        while l1 or l2 or carry:
            res = 0
            if l1: res += l1.val
            if l2: res += l2.val
            if carry: res+= carry
            carry = 0
            if res >= 10:
                carry = 1
                res = res % 10
            curr.next = ListNode(res,None)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return sentinel.next