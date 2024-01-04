### remember two things use minHeap for keeping track of kth largest element and if len minheap is less than k kust add no need to pop
### only pop when the minheap length is greater than k
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        for _ in range(k,len(self.minHeap)):
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        if len(self.minHeap)==self.k:
            heapq.heappushpop(self.minHeap,val)
        else:
            heapq.heappush(self.minHeap,val)

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
