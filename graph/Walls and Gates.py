### this questions has multiscource bfs so use of visited is for edge case
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here

        R, C = len(rooms), len(rooms[0])
        queue = []
        INF = 2147483647
        dist = 0
        visited = set()



        for r in range(R):
            for c in range(C):
                if rooms[r][c]==0:
                    queue.append([r,c])
                    

        while queue:

            for i in range(len(queue)):   
                r,c = queue.pop(0)
                if (r,c) not in visited:
                    rooms[r][c]= dist
                    visited.add((r,c))
                    if r+1<R and rooms[r+1][c]!= -1 and rooms[r+1][c]==INF:
                        queue.append([r+1,c])
                    if c+1<C and rooms[r][c+1]!= -1 and rooms[r][c+1]==INF:
                        queue.append([r,c+1])
                    if r>=1 and rooms[r-1][c]!= -1 and rooms[r-1][c]==INF:
                        queue.append([r-1,c])
                    if c>=1 and rooms[r][c-1]!= -1 and rooms[r][c-1]==INF:
                        queue.append([r,c-1])
            dist+=1


