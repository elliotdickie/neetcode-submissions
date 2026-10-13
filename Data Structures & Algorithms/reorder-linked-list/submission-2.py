# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        prev = None
        while right:
            n_ext = right.next
            right.next = prev
            prev = right
            right = n_ext
        
        left,right = head,prev
        while right:
            lnext,rnext = left.next,right.next
            left.next = right
            right.next = lnext
            left,right = lnext,rnext

        