class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        block = defaultdict(set)
        empty = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    block[3*(i//3)+(j//3)].add(board[i][j])
                else:
                    empty.append((i,j))


        def dfs(k):

            if k>=len(empty):
                return True

            row,col = empty[k]
   

            for num in map(str, range(1, 10)):
        
                if (num in rows[row]) or (num in cols[col]) or (num in block[3*(row//3)+(col//3)]):
                    continue

                board[row][col] = (num)
                rows[row].add((num))
                cols[col].add((num))
                block[3*(row//3)+(col//3)].add((num))



                if dfs(k+1):
                    return True
                else:
                    rows[row].remove((num))
                    cols[col].remove(num)
                    block[3*(row//3)+(col//3)].remove(num)

            return False
        dfs(0)
                        

            





        
