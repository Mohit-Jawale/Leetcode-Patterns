class MovingAverage:

    def __init__(self, size: int):

        self.window = []
        self.size = size
        self.sum = 0
        self.avg = 0
        self.left,self.right = 0,0
        

    def next(self, val: int) -> float:

        self.window.append(val)
        self.sum+=val
        
        if (self.right-self.left+1)<=self.size:
            self.right+=1
            return self.sum/len(self.window)
        else:
            self.sum-=self.window[self.left]
            self.right+=1
            self.left+=1
            return self.sum/self.size


            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
