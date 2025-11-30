class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:


        ### nums -> n - forgtton
        #### [x,y,.....z]

        adjList = collections.defaultdict(list)

        for u,v in adjacentPairs:
            adjList[u].append(v)
            adjList[v].append(u)
        
        start = 0

        for key,value in adjList.items():
            
            if len(adjList[key])==1:
                start = key
                break
        
        visited = set()
        visited.add(start)


        def dfs(node,ans):

            ans.append(node)
            
            for neighbour in adjList[node]:

                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour,ans)
                    

            return ans


        return dfs(start,[])



        
