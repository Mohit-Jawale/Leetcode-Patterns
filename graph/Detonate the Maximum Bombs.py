class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:


        adjList = collections.defaultdict(set)

        for index,value1 in enumerate(bombs):
            x1,y1,r1 = value1
            adjList[index]
            for index2,value2 in enumerate(bombs):
                x2,y2,r2 = value2
                if index==index2:
                    continue
                dist = sqrt((x2-x1)**2 + (y2-y1)**2)

                if dist<=r1:
                    adjList[index].add(index2)
        
        def dfs(node,visited):
                
            visited.add(node)

            for neighbour in adjList[node]:

                if neighbour not in visited:
                    dfs(neighbour,visited)
            
            return visited
            
        ans = 1

        for index,value in enumerate(bombs):
            ans = max(len(dfs(index,set())),ans)
        
        return ans
