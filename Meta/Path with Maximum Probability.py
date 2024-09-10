class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        


        adjList = collections.defaultdict(list)
        k = 0
        for i,j in edges:
            adjList[i].append((j,succProb[k]))
            adjList[j].append((i,succProb[k]))
            k+=1
        

        success = [0]*n
        queue = collections.deque([start_node])

        success[start_node]=1

        while queue:
            node = queue.popleft()

  
            for neighbour,prob in adjList[node]:

                if success[neighbour]<success[node]*prob:
                    success[neighbour] = success[node]*prob
                    queue.append(neighbour)
        
        return success[end_node] if success[end_node]!=0 else 0












