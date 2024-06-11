### topolofgical sort

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
                    queue.append((i,j))

        LIPM = 0

        while queue:
            l = len(queue)
            for _ in range(l):
                i,j = queue.popleft()
                for r,c in adjList[(i,j)]:
                    indegree[(r,c)]-=1
                    if indegree[(r,c)]==0:
                        queue.append((r,c))
            
            LIPM+=1

        return LIPM
            








### dfs+ memo
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m,n = len(matrix),len(matrix[0])

        memo = {}

        visited = set()

        def dfs(i,j,prev):

            if i<0 or j<0 or i>=m or j>=n or (i,j) in visited:
                return 0
                
            if prev>=matrix[i][j]:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            visited.add((i,j))

            right = dfs(i+1,j,matrix[i][j])+1
            left = dfs(i-1,j,matrix[i][j])+1
            up = dfs(i,j+1,matrix[i][j])+1
            down = dfs(i,j-1,matrix[i][j])+1

            visited.remove((i,j))

            memo[(i,j)] = max(right,left,up,down)

            return memo[(i,j)]

        LIPM = 1
        for i in range(m):
            for j in range(n):
                LIPM = max(dfs(i,j,-float('inf')),LIPM)
        
        return LIPM

