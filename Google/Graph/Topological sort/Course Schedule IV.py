class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:


        topological_order = []
        indegree = [0]*numCourses
        graph = collections.defaultdict(list)
        prerequisites_set = collections.defaultdict(set)

    
        for i,j in prerequisites:

            graph[i].append(j)
            indegree[j]+=1
        

        queue = collections.deque([])

        for index,value in enumerate(indegree):

            if value == 0:
                queue.append(index)
        
     
        while queue:

            node  = queue.popleft()

   

            for neighbour in graph[node]:
                
                prerequisites_set[neighbour].add(node)
                prerequisites_set[neighbour].update(prerequisites_set[node])

                indegree[neighbour]-=1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        ans = []

        for source,destination in (queries):

            if source in prerequisites_set[destination]:
                ans.append(True)
            else:
                ans.append(False)

           
        
        return ans


        
