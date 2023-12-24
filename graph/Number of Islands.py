
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        m,n = len(grid),len(grid[0])

        def dfs(i,j):

            if i<0 or i>=m or j<0 or j>=n:
                return

            if grid[i][j]=="0" or grid[i][j]==2:
                return 
            
            grid[i][j]=2

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and grid[i][j]!=2:
                    dfs(i,j)
                    count+=1
        
        return count



# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

#         R,C = len(grid), len(grid[0])

#         number_of_island = 0

#         def dfs(r,c):
#             if grid[r][c]=='1': 
#                 grid[r][c]='2'   
#                 if r>=1:dfs(r-1,c)
#                 if r+1<R:dfs(r+1,c)
#                 if c>=1:dfs(r,c-1)
#                 if c+1<C:dfs(r,c+1)

        
#         for i in range(R):
#             for j in range(C):
#                 if grid[i][j]!='2' and grid[i][j]=='1':
#                     dfs(i,j)
#                     number_of_island+=1

#         return(number_of_island)
