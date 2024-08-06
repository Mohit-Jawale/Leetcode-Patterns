class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        adjList = defaultdict(set)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+'*'+word[j+1:]
                adjList[pattern].add(word)
 
           
        queue = collections.deque([])

        queue.append((beginWord,1))
        visited = set(beginWord)

        while queue:

            node,dist = queue.popleft()

            if node == endWord:
                return dist
            
            for i in range(len(node)):
   
                pattern = node[:i]+"*"+node[i+1:]
          
                for neighbour in adjList[pattern]:
                    if neighbour not in visited:
                        queue.append((neighbour,dist+1))
                        visited.add(neighbour)
            
        return 0

        
