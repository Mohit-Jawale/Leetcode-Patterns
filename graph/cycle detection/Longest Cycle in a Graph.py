 Longest Cycle in a Graphclass Solution:
    def longestCycle(self, edges: List[int]) -> int:

        ### its a DAG 
        ### so edges cases,
        #### if disjoint or disconnected graph
        ### no self loops and no multiple edges
        ### no mutiple loops
        ### topological sort bfs

        adjList = defaultdict(list)
        indegree = [0]*len(edges)

        for i,j in enumerate(edges):
            if j!=-1:
                adjList[i].append(j)
                indegree[j]+=1
        

        queue = collections.deque([])
        
        for key,value in enumerate(indegree):
            if value == 0:
                queue.append(key)
        
        topo = []

        while queue:

            node = queue.popleft()

            topo.append(node)

            for neighbour in adjList[node]:

                indegree[neighbour]-=1

                if indegree[neighbour]==0:
                    queue.append(neighbour)
        
        
        remaining_nodes = {node for node,value in enumerate(indegree) if value>0}

        visited = set()

        def longest_cycle_bfs(parent,dist):

            nonlocal visited

            queue = collections.deque([(parent,dist)])


            while queue:

                node,dist = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)

                for neighbour in adjList[node]:

                    if neighbour == parent:
                        return dist+1

                    elif neighbour not in visited:
                        queue.append((neighbour,dist+1))

            return 0
        
        max_cycle_len = 0
        for node in remaining_nodes:

            if node not in visited:
                max_cycle_len = max(longest_cycle_bfs(node,0),max_cycle_len)


        return max_cycle_len if max_cycle_len>0 else -1



     
    





        
