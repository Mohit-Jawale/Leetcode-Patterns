class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m,n = len(matrix),len(matrix[0])

        moves = [(1,0),(-1,0),(0,-1),(0,1)]

        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(m):
            for j in range(n):
                
                for r,c in moves:
                    X,Y = i+r,j+c
                    if X>=0 and Y>=0 and X<m and Y<n and matrix[X][Y]>matrix[i][j]:
                        adjList[(i,j)].append((X,Y))
                        indegree[(X,Y)]+=1
        
        queue = collections.deque([])

        for i in range(m):
            for j in range(n):
                if (i,j) not in indegree:
                    queue.append((i,j,1))

        LIPM = 0

        while queue:
 
            i,j,path_length = queue.popleft()
            LIPM = max(LIPM,path_length)
            for r,c in adjList[(i,j)]:
                indegree[(r,c)]-=1
                if indegree[(r,c)]==0:
                    queue.append((r,c,path_length+1))
            

        return LIPM
            


         


