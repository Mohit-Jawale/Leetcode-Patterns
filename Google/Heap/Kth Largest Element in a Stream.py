from heapq import heappop,heappush,heappushpop

class KthLargest:
    #### TC -> O(Nlogk)   SC->O(K)

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
            
                
    def add(self, val: int) -> int:

        if len(self.min_heap)<self.k:
            heappush(self.min_heap,val)
        else:
            if self.min_heap[0]>=val:
                return self.min_heap[0]
            else:
                heappushpop(self.min_heap,val)
        
        return self.min_heap[0]
                
                
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
