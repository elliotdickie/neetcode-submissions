"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        old_sentinel = Node(-1,head,None)
        new_sentinel = Node(-1,None,None)

        old_curr = old_sentinel
        new_curr = new_sentinel

        while old_curr.next:
            new_curr.next = Node(old_curr.next.val,None,None)
            old_curr = old_curr.next
            new_curr = new_curr.next
            node_map[old_curr] = new_curr
        

        old_curr = old_sentinel.next
        new_curr = new_sentinel.next
        while old_curr:
            if old_curr.random: new_curr.random = node_map[old_curr.random]
            old_curr = old_curr.next
            new_curr = new_curr.next

        return new_sentinel.next