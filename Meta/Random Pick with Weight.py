class Solution:

    def __init__(self, w: List[int]):
        
        self.sum = 0
        self.prefixSum = []
        for i in w:
            self.sum+=i
            self.prefixSum.append(self.sum)
        

    def pickIndex(self) -> int:
        ran = random.randint(1,self.sum)
        left,right = 0,len(self.prefixSum)

        while left<right:

            mid = left+(right-left)//2

            if ran> self.prefixSum[mid]:
                left = mid+1
            else:
                right = mid
                
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
