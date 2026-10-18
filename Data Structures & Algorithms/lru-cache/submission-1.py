class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        
    def update(self,key,value):
        currNode = self.key_map[key]
        currNode.value = value
        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev
        tmp = self.head.next
        self.head.next = currNode
        tmp.prev = currNode
        currNode.next = tmp
        currNode.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.update(key,self.key_map[key].value)
            return (self.key_map[key].value)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #update value and place in correct position
        if key in self.key_map:
            self.update(key,value)
        else:
            currNode = Node(key,value)
            self.key_map[key] = currNode
            tmp = self.head.next
            self.head.next = currNode
            tmp.prev = currNode
            currNode.prev = self.head
            currNode.next = tmp
            self.size += 1

        #evict least recently used key
        if self.size > self.capacity:
            deadNode = self.tail.prev
            deadNode.prev.next = self.tail
            self.tail.prev = deadNode.prev
            deadKey = deadNode.key
            del(self.key_map[deadKey])
            self.size -= 1
        



