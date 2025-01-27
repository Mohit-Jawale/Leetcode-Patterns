class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        adjList = collections.defaultdict(list)
        prerequiste = collections.defaultdict(set)

        indegree = [0]*numCourses

        for i,j in prerequisites:
            adjList[i].append(j)
            indegree[j]+=1
        
        queue = collections.deque([])

        for index,value in enumerate(indegree):
            if value == 0:
                queue.append(index)
        
    
        while queue:

            node = queue.popleft()

            for neighbour in adjList[node]:

                prerequiste[neighbour].add(node)
                prerequiste[neighbour].update(prerequiste[node])
                
                indegree[neighbour]-=1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        ans = []

        for u,v in queries:

            if u in prerequiste[v]:
                ans.append(True)
            else:
                ans.append(False)

        return ans
