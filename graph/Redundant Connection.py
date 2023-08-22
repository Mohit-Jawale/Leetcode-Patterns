class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        root = [i for i in range(n)]
        rank = [1]*n
        redundant_edges = []

        def find(x):
            if x == root[x]:
                return x
            root[x]=find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]= rootX 
                    rank[rootX]+=1

            else:
                return [x+1,y+1]

        
        for i,j in edges:
            ans = union(i-1,j-1)
            if ans:
                redundant_edges.append(ans)
       
        return redundant_edges[-1]      



        
