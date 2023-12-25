### This is coloring algorithm to find cycle using 3 colors white,gray,black
### white-unvisted,gray-visiting,black-visited
### if gray is visited again that means there is cycle
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        white = 0
        gray = 1
        black = 2
 
        def dfs(i):

            if color[i]==gray:
                return True
            elif color[i]==black:
                return False

            color[i] = gray
               
            for neighbour in graph[i]:
                if dfs(neighbour):
                    return True

            color[i] = black
            return False
        
        ans = []
        color = [white]*len(graph)
        
        for node in range(len(graph)):
            if not dfs(node):
                ans.append(node)
        
        return ans

