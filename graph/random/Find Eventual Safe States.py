
#### its directed and sorted so topo

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        adjList = collections.defaultdict(list)
        indegree = [0]* n

        for i in range(n):
            for neighbour in graph[i]:
                adjList[neighbour].append(i)
                indegree[i]+=1
        
        queue = collections.deque([])

        for index,value in enumerate(indegree):
            if value==0:
                queue.append(index)
        
        topo = []
       
        while queue:
            node = queue.popleft()

            topo.append(node)

            for neighbour in adjList[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        
        topo.sort()
        return topo
            


        
        

        

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

