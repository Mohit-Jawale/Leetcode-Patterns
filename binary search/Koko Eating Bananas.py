class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        ans = right

        while left<=right:

            hours = 0
            middle = (left+right)//2

            for p in piles:
                hours+=math.ceil(p / middle)

            if hours<=h:
                ans = min(ans,middle)
                right = middle-1
            else:
                left = middle+1

        return ans                



    
