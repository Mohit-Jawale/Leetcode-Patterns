class UnionFind:

    def __init__(self,n):

        self.rank = [1]*n
        self.root = [i for i in range(n)]
    
    def find(self,x):

        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,i,j):

        rootX = self.find(i)
        rootY = self.find(j)

        if rootX != rootY:

            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1



class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        uf = UnionFind(n)

        for i in range(1,n):

            if nums[i]-nums[i-1]<=maxDiff:
                uf.union(i,i-1)
        
        ans = []

        for i,j in queries:

            if  uf.find(i) == uf.find(j):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans


        

        

        
        
    
