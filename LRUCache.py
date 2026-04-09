class Node:
    def __init__(self, key , val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class Cache:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)  #dummy nodes

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self , node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def put(self , key : int , val : int) -> int:
        if key in self.cache :
            self.remove(self.cache[key])

        self.cache[key] = Node(key,val)
        self.insert(self.cache[key])    # from right side MRU

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]


    def get(self, key:int)-> int:
        if key in self.cache :
            self.remove(self.cache[key])
            self.insert(self.cache[key])  # mru right side 

            return self.cache[key].val
        return -1 




