# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #put a pointer on each list
        #move up list 1, inserting list2 where it fits
        head = ListNode(-1,None)
        curr = head
        while list1 or list2:
            if list1 and (not list2 or list2.val > list1.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        return head.next
