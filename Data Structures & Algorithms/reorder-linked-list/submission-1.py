# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #last node becomes 2nd node
        #second node becomes third node
        if not head or not head.next: return
        left,right = head.next,head.next
        
        length=1
        while right:
            length+=1
            right = right.next
        
        right = left
        index = 1
        while index < length//2:
            right = right.next
            index+=1

        n_ext = right.next
        right.next = None
        prev = right
        right = n_ext
        while right:
            n_ext = right.next
            right.next = prev
            prev = right
            right = n_ext
        right = prev

        head.next = right
        while left != right:
            n_ext = right.next
            right.next = left
            right = n_ext
            if left:
                n_ext = left.next
                left.next = right
                left = n_ext
        