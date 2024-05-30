class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m , n = len(board), len(board[0])
        visited = set()

        def backtracking(r,c,k):

            if k == len(word):
                return True
      
            if r<0 or c<0 or c>=n or r>=m or (r,c) in visited:
                return False
    
            if board[r][c]==word[k]:

                visited.add((r,c))

                down = dfs(r+1,c,k+1)
                up = dfs(r-1,c,k+1)
                right = dfs(r,c+1,k+1)
                left = dfs(r,c-1,k+1)

                visited.remove((r,c))

                if down or up or right or left:
                    return True
       
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        
        return False
        
