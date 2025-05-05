class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #### find out the boundary node
        ### apply dfs on it and mark all the O to #
        ### now mark reamining o to X and then # back to 0

        ### TC - >O(m*n)  SC= (m*n)



        ROWS, COLS = len(board), len(board[0])

        boundary_node = []

        for row in range(ROWS):
            for col in range(COLS):

                if board[row][col]== "O" and (row==0 or col==0 or row==ROWS-1 or col==COLS-1):
                    boundary_node.append((row,col))
        

        def dfs(row,col):

            if not (row>=0 and col>=0 and row<ROWS and col<COLS):
                return

            if board[row][col] == "X":
                return

            if board[row][col] == "O":

                board[row][col] = "#"

                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)

        for r,c in boundary_node:
            dfs(r,c)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]=='O':
                    board[row][col]= 'X'
                if board[row][col]=='#':
                    board[row][col]='O'
                


            



        


        
