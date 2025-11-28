
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.lru = Node("#",-1)
        self.mru = Node("*",-1)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.lookup = {}
        

    def removeKey(self,key):
        
        nodeRef = self.lookup[key]
        nodeRef.prev.next = nodeRef.next
        nodeRef.next.prev = nodeRef.prev
        return nodeRef
    
    def insertNode(self,newNode):
        lastNode = self.mru.prev
        self.mru.prev = newNode
        newNode.next = self.mru
        newNode.prev = lastNode
        lastNode.next = newNode
    
    def get(self, key: int) -> int:
        if key in self.lookup:
            tempNode = self.removeKey(key)
            self.insertNode(tempNode)
            return self.lookup[key].value
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        
        if key in self.lookup:

            tempNode=self.removeKey(key)
            tempNode.value = value
            self.lookup[key] = tempNode
            self.insertNode(tempNode)
        else:
            if len(self.lookup)<self.capacity:
                newNode = Node(key,value)
                self.insertNode(newNode)
                self.lookup[key] = newNode
            else:
                removedNode = self.removeKey(self.lru.next.key)
                del self.lookup[removedNode.key]
                self.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
