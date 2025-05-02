class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        Rows,Cols = len(mat), len(mat[0])
        distance = [[float('inf') for _ in range(Cols)] for _ in range(Rows)]

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        queue = collections.deque([])

        for i in range(Rows):
            for j in range(Cols):

                if mat[i][j]==0:
                    queue.append((i,j))
                    distance[i][j] = 0


        while queue:

            x,y = queue.popleft()

            for i,j in directions:
                newX,newY = i+x, j+y

                if newX>=0 and newX<Rows and newY>=0 and newY<Cols:

                    if distance[newX][newY]>distance[x][y]+1:
                        distance[newX][newY] = distance[x][y]+1
                        queue.append((newX,newY))


        return distance
