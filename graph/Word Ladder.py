class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        adj_list = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+'*'+word[j+1:]
                adj_list[pattern].append(word)

        queue = []
        queue.append(beginWord)
        visited =set(beginWord)
        res = 1

        while queue:

            for i in range(len(queue)):
             
                word = queue.pop(0)

                if word == endWord:
                    return res
                    
                for j in range(len(word)):
                    pattern = word[:j]+'*'+word[j+1:]
                    for neighbour in adj_list[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)

            res+=1
        return 0    

  




        
