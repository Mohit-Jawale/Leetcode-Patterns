### see how lazy deleted is done here 
class StockPrice:

    def __init__(self):
        self.price = {}
        self.maxHeap = []
        self.minHeap = []
        self.index = 0
        self.deleted = set()
        self.currTimeStamp = 0

        

    def update(self, timestamp: int, price: int) -> None:

        if timestamp in self.price:
            self.deleted.add(self.price[timestamp][1])
          
        self.price[timestamp] = (price,self.index)

        heapq.heappush(self.maxHeap,(-1*price,self.index))
        heapq.heappush(self.minHeap,(price,self.index))

        self.currTimeStamp = max(self.currTimeStamp,timestamp)
        self.index+=1
    

                    

    def current(self) -> int:
        return self.price[self.currTimeStamp][0]
        

    def maximum(self) -> int:
        while self.maxHeap and self.maxHeap[0][1] in self.deleted:
            heapq.heappop(self.maxHeap)
        
        return -self.maxHeap[0][0]
        

    def minimum(self) -> int:

        while self.minHeap and self.minHeap[0][1] in self.deleted:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
