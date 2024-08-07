class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        memo = {}

        def dfs(i):
            
            if i>=len(books):
                return 0
            if i in memo:
                return memo[i]
            maxHeight = 0
            currWidth = shelfWidth

            res = float('inf')

            for k in range(i,len(books)):
                width,height = books[k]
                if currWidth < width:
                    break
                currWidth-=width
                maxHeight = max(height,maxHeight)
                res = min(res,dfs(k+1)+maxHeight)

            memo[i] = res

            return res
        
        return dfs(0)
               
