class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [-1]*len(graph)

        white = 0
        black = 1
        
        for i in range(len(graph)):

            if color[i]==-1:

                queue = [i]
                color[i]=white

                while queue:
                    node = queue.pop(0)

                    for neighbour in graph[node]:
                        if color[neighbour]==-1:
                            color[neighbour] = black if color[node]==white else white
                            queue.append(neighbour)
                        elif color[neighbour]==color[node]:
                            return False
        
        return True
