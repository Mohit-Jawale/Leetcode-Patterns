class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        
        root = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]



        def union(x,y):
            nonlocal components
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX]=rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                components-=1

        for i,j in edges:
            union(i,j)
        print(components)
        return components    
