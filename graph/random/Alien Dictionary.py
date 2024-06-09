class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for w in words:
            for char in w:
                if char in adjList:
                    continue
                adjList[char]

                indegree[char]=0


        for i in range(len(words)-1):

            w1,w2 = words[i],words[i+1]
            found = False
            
            for j in range(min(len(w1),len(w2))):

                if w1[j]!=w2[j]:
                    adjList[w1[j]].append(w2[j])
                    indegree[w2[j]]+=1
                    found = True
                    break
                
            if found == False and len(w1)>len(w2):
                return ""
        

        queue = collections.deque([])
        ans = ""

        for key,value in indegree.items():
            if value==0:
                queue.append(key)

        while queue:
            node = queue.popleft()
            ans+=node

            for neighbour in adjList[node]:
                indegree[neighbour]-=1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        print(ans)
        if len(ans)<len(adjList):### for detecting cycle
            return ""
        return ans




