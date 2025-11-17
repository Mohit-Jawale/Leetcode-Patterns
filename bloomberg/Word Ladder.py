class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        wordList.append(beginWord)

        wordDict = collections.defaultdict(list)

        for word in wordList:

            for j in range(len(word)):

                pattern = word[:j]+'*'+ word[j+1:]

                wordDict[pattern].append(word)
        
        queue = collections.deque([[beginWord,1]])

        visited = set()
        visited.add(beginWord)
        
        while queue:

            word,length = queue.popleft()


            if word == endWord:
                return length
            
            for j in range(len(word)):

                pattern = word[:j]+'*'+word[j+1:]
                for nextWord in wordDict[pattern]:
                    if nextWord not in visited:
                        queue.append([nextWord,length+1])
                        visited.add(nextWord)
        
        return 0


            

         
