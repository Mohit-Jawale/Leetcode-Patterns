class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m,n = len(grid),len(grid[0])

        def dfs(i,j):

            nonlocal count
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]==0 or grid[i][j]=='#':
                return
            
            grid[i][j]='#'
            count+=1
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and grid[i][j]!='#':
                    count=0
                    dfs(i,j)
                    ans = max(ans,count)
               
        return ans
                    

        


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         R, C = len(grid), len(grid[0])

#         count = 0
#         max_area = 0
#         def dfs(r,c):
#             nonlocal count

#             if grid[r][c]==1:

#                 grid[r][c] = 2
#                 count+=1
#                 if r+1<R:dfs(r+1,c)
#                 if c+1<C:dfs(r,c+1)
#                 if r>=1:dfs(r-1,c)
#                 if c>=1:dfs(r,c-1)


#         for r in range(R):
#             for c in range(C):
#                 if grid[r][c] == 1:
#                     count = 0
#                     dfs(r,c)
#                     max_area = max(max_area,count)

#         return max_area            




        
