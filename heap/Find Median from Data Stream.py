### refer this for explanation-:https://leetcode.com/problems/find-median-from-data-stream/solutions/74047/java-python-two-heap-solution-o-log-n-add-o-1-find/

import heapq as hq
class MedianFinder:

    def __init__(self):

        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.maxHeap)==len(self.minHeap):
            hq.heappush(self.minHeap,-hq.heappushpop(self.maxHeap,-num))
        else:
            hq.heappush(self.maxHeap,-hq.heappushpop(self.minHeap,num))    


    def findMedian(self) -> float:
        if len(self.minHeap)==len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        else:
            return self.minHeap[0]    

    
