class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        #### key observation is this is DAG so no need of visited set
        ans = []
        destination = len(graph)-1

        visited = set()

        def dfs(source,path):

            if source == destination:
                ans.append(copy.deepcopy(path))
                return
            
            for neighbour in graph[source]:
                    dfs(neighbour,path+[neighbour])

            
        dfs(0,[0])
        return ans
        
