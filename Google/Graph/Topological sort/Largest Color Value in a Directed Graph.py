class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:


        ### there is DG 0 to n-1

        ### what if there is cycle or self loop in that case there is not direct path

        ### can there be multiple componenets? 

        #### topo sort why? bcz we will be sure that we have explored all the node before that node
        #### we can find the vaild path using bfs level by level
        ### what if there is vaild path and cycle topo sort might not work bcz it stops as soon
        ### as there is cycle in graph return -1
        ### colors hashmap

        ###3 tc -: O(26(V+E)) and sc-: O(26N)


        max_color_dict = collections.defaultdict(Counter)

        queue = collections.deque([])

        graph = collections.defaultdict(list)

        indegree  = [0]* len(colors)


        for src,dst in edges:
            graph[src].append((dst))
            indegree[dst]+=1
        
        for index,value  in enumerate(indegree):

            if value == 0 :
                queue.append((index,colors[index]))
        

        topological_order = []

        while queue:

            node, node_color = queue.popleft()

            topological_order.append(node)
            max_color_dict[node][node_color]+=1 
                      

            for neighbour in graph[node]:

                for i in range(26):

                    max_color_dict[neighbour][chr(i+97)] = max(max_color_dict[node][chr(i+97)],max_color_dict[neighbour][chr(i+97)])
                    
                indegree[neighbour]-=1
                
                if indegree[neighbour]==0:
                    
                    queue.append((neighbour,colors[neighbour]))

        if len(topological_order)!=len(colors):
            return -1

        max_color = 0

        for i in range(len(colors)):

            max_color= max(max_color_dict[i].most_common(1)[0][1],max_color)
        
        return max_color

        
        






