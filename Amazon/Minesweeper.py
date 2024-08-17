class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:


        m,n = len(board),len(board[0])

        moves = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    

        queue = collections.deque([])

        queue.append(click)

        while queue:
            i,j = queue.popleft()

            if board[i][j]=='E':
                count = 0
                temp = []
                for r,c in moves:
                    ai,aj = i+r,j+c
                    if not (ai<0 or aj<0 or ai>=m or aj>=n):
                        if board[ai][aj]=='E':
                            temp.append((ai,aj))
                            continue
                        elif board[ai][aj]=='M':
                            count+=1
                if count>0:
                    board[i][j]=str(count)
                else:
                    board[i][j]="B"
                    queue+=temp

            elif board[i][j]=="M":
                board[i][j]="X"

        
        return board
                    
                
