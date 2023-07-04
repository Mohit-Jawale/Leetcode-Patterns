class MinStack:

    def __init__(self):
        self.minstack = []
        self.minelement = []


    def push(self, val: int) -> None:
        if self.minelement:
            self.minelement.append(min(self.minelement[-1],val))
        else:
            self.minelement.append(val)    
        self.minstack.append(val)     

    def pop(self) -> None:
        self.minstack.pop()
        self.minelement.pop()
        

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        return self.minelement[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
