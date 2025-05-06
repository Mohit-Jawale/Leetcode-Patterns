class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #### TC - O(V+E) SC- O(V) 
        #### remeber ever is travsed jst once 
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




        
