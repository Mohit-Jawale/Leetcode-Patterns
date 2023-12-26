### the approach mentioned below is unique way of implementing bfs on matrix, it saves memory of visited nodes and extra matrix for ans
### pretty smart approach

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        m,n = len(mat), len(mat[0])
        
        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]= float('inf')

        while queue:

            r,c = queue.pop(0)

            for i,j in moves:
                ai,aj = r+i,c+j
                if not (ai<0 or ai>=m or aj<0 or aj>=n) and mat[ai][aj]>mat[r][c]+1:
                    mat[ai][aj]=mat[r][c]+1
                    queue.append((ai,aj))
        
        return mat

                    


