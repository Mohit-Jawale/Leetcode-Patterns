class MaxStack:

    def __init__(self):

        self.stack = []
        self.removedElment = set()
        self.maxHeap = []
        self.stackIdx = 0
        

    def push(self, x: int) -> None:
        self.stack.append((x,self.stackIdx))
        heapq.heappush(self.maxHeap,(-x,-self.stackIdx))
        self.stackIdx+=1
        

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removedElment:
            self.stack.pop()
        num,index = self.stack.pop()
        self.removedElment.add(index)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removedElment:
            self.stack.pop()
        return self.stack[-1][0]
        

    def peekMax(self) -> int:

        while self.maxHeap  and -self.maxHeap[0][1] in self.removedElment:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def popMax(self) -> int:

        while self.maxHeap  and -self.maxHeap[0][1] in self.removedElment:
            heapq.heappop(self.maxHeap)

        num,popIndex = self.maxHeap[0]

        if self.stack and self.stack[-1][1]==-popIndex:
            return self.pop()
        else:
            heapq.heappop(self.maxHeap)
            self.removedElment.add(-popIndex)
            return -num


        

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
