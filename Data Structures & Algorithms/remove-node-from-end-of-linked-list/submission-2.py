# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 1
        curr = head
        while curr:
            curr = curr.next
            list_len += 1
        target = list_len-n

        pos = 1
        curr = head
        prev = None
        while pos < target:
            prev = curr
            curr = curr.next
            pos += 1
        if prev: prev.next = curr.next
        if curr == head: head=head.next
        return head
