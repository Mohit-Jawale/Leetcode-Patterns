#### Frist plan then code also insert into dll from head and remove from tail i.e mru is at head and lru is at tail




class Node:
    def __init__(self,key,value):
        self.key, self.value = key, value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = Node(-1,-1)
        self.mru = Node(-1,-1)
        self.cache = {}
        self.mru.prev, self.lru.next = self.lru, self.mru


    def remove(self,node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self,node):
        prev, next = self.mru.prev, self.mru
        node.next, node.prev = next, prev
        next.prev = prev.next = node
        


    def get(self, key: int) -> int:a
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1    
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])    

        if len(self.cache)>self.capacity:
            node = self.lru.next
            self.remove(node)
            del self.cache[node.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
