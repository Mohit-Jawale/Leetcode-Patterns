
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        R , C = len(heights), len(heights[0])
        pacific,atlanic = set(),set()
 
        def dfs(gset,r,c,prevHeight):


            if prevHeight<=heights[r][c] and (r,c) not in gset:
                
                gset.add((r,c))
                if r+1<R : dfs(gset,r+1,c,heights[r][c]) 
                if c+1<C : dfs(gset,r,c+1,heights[r][c])
                if r>=1 : dfs(gset,r-1,c,heights[r][c])
                if c>=1 : dfs(gset,r,c-1,heights[r][c])
   

        for c in range(C):
            dfs(pacific,0,c,heights[0][c])
            dfs(atlanic,R-1,c,heights[R-1][c])

        for r in range(R):
            dfs(pacific,r,0,heights[r][0])
            dfs(atlanic,r,C-1,heights[r][C-1])    


        ans = atlanic.intersection(pacific)
        return ans    
        
