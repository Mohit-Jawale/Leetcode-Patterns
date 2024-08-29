class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        n = len(edges)
        adjList = collections.defaultdict(list)

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        for i in range(1,n+2):
            if i in adjList and len(adjList[i])==n:
                return i
        
        

        
