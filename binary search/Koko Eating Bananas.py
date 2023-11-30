class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def feasible(mid):

            minH = 0
            for pile in piles:
                temp = ceil(pile/mid)
                minH+=temp
            if minH<=h:
                return True    
             

        left,right = 1,max(piles)

        while left<right:
            mid = left+(right-left)//2

            if feasible(mid):
                right = mid
            else:
                left = mid+1

        return left            
