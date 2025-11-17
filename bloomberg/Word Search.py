class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:




        def dfs(r,c,wordPtr,visited):
            

            if wordPtr == len(word):
                return True

            if r<0 or c<0 or r>=len(board) or c>=len(board[0]):
                return False
            
            if (r,c) in visited:
                return False
            

            if board[r][c]==word[wordPtr]:
                visited.add((r,c))

                up = dfs(r+1,c,wordPtr+1,visited)
                down = dfs(r,c+1,wordPtr+1,visited)
                right = dfs(r-1,c,wordPtr+1,visited)
                left = dfs(r,c-1,wordPtr+1,visited)
                

                visited.remove((r,c))

                return up or down or right or left
                
            return False
        

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c]==word[0]:
                    if dfs(r,c,0,set()):
                        return True

        return False

        
