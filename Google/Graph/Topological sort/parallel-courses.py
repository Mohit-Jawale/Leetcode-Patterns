class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #https://leetcode.com/problems/parallel-courses/description/
        #### 1-n 
        #### relations = [[1,3],[2,3]]

        #### bfs with some order traversal -> topo kahn's algorithm

        #### DAG

        #### 1 : [3]
        #### 2:  [3]

        #### TC O(V+E) SC = O(N)

        indegree = [0] * (n+1)

        graph = collections.defaultdict(list)

        topological_order = []

        queue = collections.deque([])

        for prevCourse,nextCourse in relations:

            graph[prevCourse].append(nextCourse)
            indegree[nextCourse]+=1
        
        for index,value in enumerate(indegree):
            if value == 0 and index!=0:
                queue.append((index,1)) ###(node,current_semester)
        

        while queue:

            node,curr_sem = queue.popleft()

            topological_order.append(node)

            for neighbour in graph[node]:

                indegree[neighbour]-=1

                if indegree[neighbour]==0:
                    queue.append((neighbour,curr_sem+1))
        

        return curr_sem if len(topological_order)==n else -1


        

