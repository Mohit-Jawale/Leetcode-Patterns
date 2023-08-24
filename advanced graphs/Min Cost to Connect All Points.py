class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        mincost = []
        ### O(N^2)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                val =  abs(abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1]))
                mincost.append((i,j,val)) 

        ### O(NlogN)       
        mincost = sorted(mincost, key = lambda x:x[2])  
   
        root = [i for i in range(len(points))]
        rank = [1]*len(points)
        cost = 0
        ans = 0


        def find(x):
            if x == root[x]:
                return x
            root[x]= find(root[x])
            return root[x]

        def union(x,y,val):

            nonlocal ans
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX]= rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                ans+=val

        for node in mincost:
            s, d, weight = node
            union(s,d,weight)

        return ans    
                      
                                      
                      




