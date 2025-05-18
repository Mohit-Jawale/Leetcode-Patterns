from heapq import heappush,heappop,heappushpop
class MedianFinder:

    def __init__(self):

        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:

        if len(self.min_heap)==len(self.max_heap):

            heappush(self.min_heap,-heappushpop(self.max_heap,-num))
        else:
            heappush(self.max_heap,-heappushpop(self.min_heap,num))
        

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):

            return (self.min_heap[0]-self.max_heap[0])/2
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
