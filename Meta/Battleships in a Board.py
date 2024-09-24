class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        rows,cols = len(board),len(board[0])


        def dfs(r,c):
            
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            
            if board[r][c]=='.' or board[r][c]=='#':
                return 
            
            if board[r][c]=='X':

                board[r][c] = '#'
                
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)
        


        count = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='X':
                    dfs(i,j)
                    count+=1
        
        return count


        
