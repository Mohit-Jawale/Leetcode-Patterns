class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)

        indegree = [0]* numCourses

        queue = []

        for i,j in prerequisites:
            adj_list[j].append(i)
            indegree[i]+=1

        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        topo = []
        while queue:
            node = queue.pop(0)
            topo.append(node)
            for neighbour in adj_list[node]:
                indegree[neighbour]-=1 
                
                if indegree[neighbour]==0:
                    queue.append(neighbour)

        if len(topo)==numCourses:
            return topo

        return []                      



        
