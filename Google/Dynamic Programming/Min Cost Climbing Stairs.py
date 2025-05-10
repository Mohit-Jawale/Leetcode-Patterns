class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        #### [10,15,20]

        #### 0 or 1 after paying the cost I can move to next florr by taking either 1 step or 2 step

        #### min cost #### minizinag


        ### top floor -> top floor   cost 45. cost 30->15
        ##### step2 ->>>>> 20      step2-> 10
        ####. step 1->>>> 15.  step 1. 15
        ###   step 0 ->>>> 10. 
        #### step -1

        memo = {}

        def findMinCostToClimbToTopFloor(i):

            if i>=len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            

            stepOne = findMinCostToClimbToTopFloor(i+1)+cost[i]
            stepTwo = findMinCostToClimbToTopFloor(i+2)+cost[i]

            memo[i] = min(stepOne, stepTwo)

            return min(stepOne, stepTwo)
        
        startsWithZero = findMinCostToClimbToTopFloor(0)
        memo = {}
        startsWithFirst = findMinCostToClimbToTopFloor(1)

        return min(startsWithZero,startsWithFirst)
        







        
