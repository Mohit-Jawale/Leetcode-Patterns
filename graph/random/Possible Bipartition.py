from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        if not dislikes:
            return True

        adjList = defaultdict(list)

        for i, j in dislikes:
            adjList[i].append(j)
            adjList[j].append(i)  # This is important to add the reverse edge as well.

        white, black = 0, 1

        color = [-1] * (n + 1)

        for node in range(1, n + 1):
            if color[node] == -1:
                queue = deque([node])
                color[node] = white

                while queue:
                    current = queue.popleft()

                    for neighbour in adjList[current]:
                        if color[neighbour] == -1:
                            color[neighbour] = black if color[current] == white else white
                            queue.append(neighbour)
                        elif color[neighbour] == color[current]:
                            return False

        return True
