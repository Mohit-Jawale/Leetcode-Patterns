class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R, C = len(board), len(board[0])
        start = word[0]
        starting = []
        visited = set()
        i = 0

        for r in range(R):
            for c in range(C):
                if start == board[r][c]:
                    starting.append([r,c])

        ans = False

        def dfs(r,c,match,i):
            
            nonlocal ans,visited

            if (r,c) in visited:
                return

            if match-1 == 0:
                ans = True 
                return 

            visited.add((r,c))        

            if r+1<R and board[r+1][c] == word[i+1]:
           
                dfs(r+1,c,match-1,i+1)
                

            if c+1<C and board[r][c+1] == word[i+1]:
                dfs(r,c+1,match-1,i+1)
 

            if r>=1 and board[r-1][c] == word[i+1]:
                dfs(r-1,c,match-1,i+1) 


            if c>=1 and board[r][c-1] == word[i+1]:
                dfs(r,c-1,match-1,i+1)

            visited.remove((r,c))

        for i,j in starting:
            dfs(i,j,len(word),0)
            visited = set()
            if ans == True:
                return ans

        return ans
                    





                      

        
