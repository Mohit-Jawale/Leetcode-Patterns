class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS,COLS = len(board), len(board[0])

        def wordSearch(row,col,visited,wordptr):

            if wordptr == len(word):
                return True

            if not(row>=0 and  col>=0 and row<ROWS and col<COLS):
                return False
            
            if (row,col) in visited:
                return False
            

            if board[row][col] == word[wordptr]:

                visited.add((row,col))

                up = wordSearch(row+1,col,visited,wordptr+1)
                down = wordSearch(row-1,col,visited,wordptr+1)
                left = wordSearch(row,col+1,visited,wordptr+1)
                right = wordSearch(row,col-1,visited,wordptr+1)

                visited.remove((row,col))

                return up or down or left or right
            
            return False
        
        
        for i in range(ROWS):
            for j in range(COLS):

                if wordSearch(i,j,set(),0):
                    return True
        
        return False


        
