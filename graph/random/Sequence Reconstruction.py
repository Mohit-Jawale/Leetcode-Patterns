class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        indegree = collections.defaultdict(int)
        adjList = collections.defaultdict(list)

       

        for seq in sequences:
            if seq[0] not in indegree:
                indegree[seq[0]]=0
            for i in range(1,len(seq)):
                indegree[seq[i]]+=1
                adjList[seq[i-1]].append(seq[i])
        

        queue = collections.deque([])

        for key,value in indegree.items():
            
            if value == 0:
                queue.append(key)
        
        topo = []
        while queue:

            if len(queue)==2:
                return False

            node = queue.popleft()

            topo.append(node)

            for neighbour in adjList[node]:
                indegree[neighbour]-=1

                if indegree[neighbour]==0:
                    queue.append(neighbour)
           
        
        if topo == nums:
            return True
        return False

        

        
