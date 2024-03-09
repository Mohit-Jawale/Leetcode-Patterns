class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        


        ### handle edge case where the source and target are same no need to take bus
        if source == target:
            return 0


        route_to_bus_mapping = defaultdict(list)
        adjList = defaultdict(set)

        ####getting the bus number from the bus stop
        for index,stops in enumerate(routes):
            for s in stops:
                route_to_bus_mapping[s].append(index)


        starting_bus_stop = route_to_bus_mapping[source]
        target_bus_stop = route_to_bus_mapping[target]

        #### make adjlist of the bus stops as from 0->1->2->0
        for index,stops in enumerate(routes):
            for s in stops:
                for bus in route_to_bus_mapping[s]:
                    if bus!=index:
                        adjList[index].add(bus)
    
        
        queue = collections.deque([])

        for startNode in starting_bus_stop:
            queue.append([startNode,1])

        visited = set()

        while queue:

            node,dist= queue.popleft()
         
            if node in target_bus_stop:
                return dist
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    queue.append([neighbour,dist+1])


        return -1
       
        
