import random
class Solution:

    def __init__(self, w: List[int]):

        self.total_weight = 0

        self.prefix_sum = []

        for weight in w:
            self.total_weight+=weight
            self.prefix_sum.append(self.total_weight)

        
    def pickIndex(self) -> int:

        target = random.randint(1,self.total_weight)

        left,right = 0,len(self.prefix_sum)

        ### lower bound
        while left<right:

            mid = left+(right-left)//2

            if self.prefix_sum[mid]>=target:
                right = mid
            else:
                left = mid+1
                
        return left


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
