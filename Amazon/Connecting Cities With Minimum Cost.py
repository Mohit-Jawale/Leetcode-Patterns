class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:


        ### union-find alogorithm to connect components using minHeap
        root = [i for i in range(n+1)]
        rank = [0]*(n+1)


        components = n
        minCost = 0

        def find(x):
            if x == root[x]:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):

            nonlocal components
            rootX = find(x)
            rootY = find(y)

            if rootX!=rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootY]>rank[rootX]:
                    root[rootX]=rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1

                components-=1
                return True

            return False ### to avoid cycle

        minHeap = [(cost,i,j) for i,j,cost in connections]

        heapq.heapify(minHeap)


        while components>1 and minHeap:
            cost,i,j = heapq.heappop(minHeap)
            if union(i,j):
                minCost+=cost
           
        return minCost if components==1 else -1
