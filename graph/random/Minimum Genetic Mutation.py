class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        

        adjList =defaultdict(set)
        bank.append(startGene)
        for b in bank:
            for r in bank:
                if b==r:
                    continue
                diff = 0
                for i in range(len(b)):
                    if b[i]!=r[i]:
                        diff+=1
                if diff==1:
                    adjList[b].add(r)
                    adjList[r].add(b)
        
        
        queue = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)

        while queue:
            currentGene, mutations = queue.popleft()
            if currentGene == endGene:
                return mutations

            for neighbor in adjList[currentGene]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, mutations + 1))


        return -1
        

                
