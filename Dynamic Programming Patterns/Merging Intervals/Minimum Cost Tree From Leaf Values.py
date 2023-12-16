class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        memo = {}
        
        def dfs(left,right):

            if (left,right) in memo:
                return memo[(left,right)]

            if left==right:
                return 0

            if left+1 == right:
                return arr[left]*arr[right]


            minSum = float('inf')

            for p in range(left,right):
                minSum = min(dfs(left,p)+dfs(p+1,right)+(max(arr[left:p+1])*max(arr[p+1:right+1])),minSum)

            memo[(left,right)] = minSum
            
            return minSum


        return dfs(0,len(arr)-1)        
            

                


        
        
