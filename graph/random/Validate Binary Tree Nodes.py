###Note -: this problem is well-designed and has multiple edges cases BE CAREFUL!!!

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        adjList = defaultdict(set)
        indegree = [0]*n
        ### make graph with indegree bcz root nodes will have zero indegree
        for i in range(n):
            adjList[i].add(leftChild[i])
            adjList[i].add(rightChild[i])
            if leftChild[i]>=0:
                indegree[leftChild[i]]+=1
            if rightChild[i]>=0:
                indegree[rightChild[i]]+=1
        
        ### find root nodes if there are multiple root nodes then there are multiple components
        rootNodes = []
        for index,value in enumerate(indegree):
            if value==0:
                rootNodes.append(index)
        
        ## there are loops in graph which will not result in tree
        if not rootNodes:
            return False

        visited = set()
        ans = True
        ## check if we can visit all nodes without runing into loop in one component
        def dfs(node):
            nonlocal ans
           
            if node == -1:
                return

            if node in visited:
                ans = False

            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour)
                else:
                    ans = False
        
    
        dfs(rootNodes[0])

        ### this condition is necessary to identify if there are mutiple components with loop
        if len(visited)==n and ans:
            return True
        return False
