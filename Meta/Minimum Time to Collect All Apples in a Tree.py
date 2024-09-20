class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:


        adjList = collections.defaultdict(list)

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        

        def dfs(node,parent):

            total = 0

            for neighbour in adjList[node]:

                if neighbour!=parent:

                    cost_of_subtree = dfs(neighbour,node)
                    if cost_of_subtree or hasApple[neighbour]:
                        total += cost_of_subtree+2

            return total
        
        return dfs(0,-1)

                
        

        
        


            


