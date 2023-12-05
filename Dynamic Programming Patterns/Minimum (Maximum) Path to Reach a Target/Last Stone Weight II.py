### This problem has lots of clear tricks...spliting to two piles
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        totalWeight = sum(stones)

        HalfTotalWeight = ceil(totalWeight/2)
    
        memo = {}
        def dfs(i,total):

            if total>=HalfTotalWeight or i>=len(stones):
                return abs(total - (totalWeight-total))
            if (i,total) in memo:
                return memo[(i,total)]

            takeStone = dfs(i+1,total+stones[i])
            dropStone = dfs(i+1,total)
            memo[(i,total)] = min(takeStone ,dropStone) 
            return  min(takeStone ,dropStone) 

           

        return dfs(0,0)    
