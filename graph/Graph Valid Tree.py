class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here



        root = [i for i in range(n)]
        rank = [1] * n
        components = n
        ans = 0

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            nonlocal components ,ans
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY]= rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX] = rootY  
                else:
                    root[rootY] = rootX   
                    rank[rootX]+=1
                components-=1 
             
            else:
                ans+=1

        for i, j in edges:
            union(i,j)
   
        if components==1 and ans==0:
            return True

        return False   
