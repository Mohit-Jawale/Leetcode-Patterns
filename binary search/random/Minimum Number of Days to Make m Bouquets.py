class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay)<m*k:
            return -1

        def feasible(currDay):
            totalflower = 0
            bouquets = 0

            for bloom in bloomDay:

                if currDay<bloom:
                    totalflower = 0
                else:
                    bouquets += (totalflower+1)//k
                    totalflower = (totalflower+1)%k
                    

            return bouquets>=m            


        left,right = min(bloomDay),max(bloomDay)

        while left<right:
            mid = left+(right-left)//2

            if feasible(mid):
                right = mid
            else:
                left = mid+1

        return left            


        
