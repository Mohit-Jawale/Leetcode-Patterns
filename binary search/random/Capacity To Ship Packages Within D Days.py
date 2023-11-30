### refer to this -:https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(capacity):
            mindays = 1
            total = 0
            for weight in weights:
                total+=weight
                if total>capacity:
                    total = weight
                    mindays+=1
                    if mindays>days:
                        return False

            return True            

        left,right = max(weights),sum(weights)

        while left<right:
            mid = left+(right-left)//2

            if feasible(mid):
                right = mid
            else:
                left = mid+1

        return left                

        
