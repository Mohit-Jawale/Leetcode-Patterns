class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1 or len(edges)==0:
            return [0]
        indegree =  collections.defaultdict(int)

        adjList = collections.defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        

        leaves = collections.deque([])

        ### find the leaves nodes

        for key,value in adjList.items():
            if indegree[key]==1:
                leaves.append(key)
        
        
        remaining_node = len(adjList)

        while remaining_node>2:

            remaining_node-=len(leaves)

            new_leaves = []
            
            for leaf in leaves:
                neighbour = adjList[leaf].pop()
                adjList[neighbour].remove(leaf)

                if len(adjList[neighbour])==1:
                    new_leaves.append(neighbour)
            
            leaves = new_leaves
        

        return leaves


                
                
    







        
