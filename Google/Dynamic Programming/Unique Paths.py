class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #### down (i+1,j) or right (i,j+1)
        ### 
        memo = {}

        def total_unique_paths(row,col):

            if not(row>=0 and col >=0 and row<m and col<n):
                return 0
            if row == m-1 and col==n-1:
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]

            down = total_unique_paths(row+1,col)
            right = total_unique_paths(row,col+1)

            memo[(row,col)] = down+right
            return down+right

        return total_unique_paths(0,0)
            
            
        
