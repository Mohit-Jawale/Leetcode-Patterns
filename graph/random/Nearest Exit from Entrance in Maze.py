class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        moves = [(1,0),(0,1),(-1,0),(0,-1)]

        ROW,COL  = len(maze),len(maze[0])
        queue = collections.deque([entrance])

        ei,ec = entrance
        maze[ei][ec]=0

        while queue:
            i,j = queue.popleft()

            for r,c in moves:
                newr = i+r
                newc = j+c
                
                if not(newr<0 or newc<0 or newr>=ROW or newc>=COL) and maze[newr][newc]=='.':

                    maze[newr][newc] = maze[i][j]+1
                    queue.append([newr,newc])
                    if (newr==0 or newc==0 or newr==ROW-1 or newc==COL-1) and [newr,newc]!=entrance and not maze[newr][newc]=='.' and not maze[newr][newc]=='+' :
                        return maze[newr][newc]            
        
        return -1
   
         
