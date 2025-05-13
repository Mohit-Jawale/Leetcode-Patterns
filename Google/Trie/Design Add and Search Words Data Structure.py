class TrieNode:

    def __init__(self):

        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root

        for char in word:

            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.end_of_word = True
        

    def search(self, word: str) -> bool:
        
        curr = self.root

        def dfs(i,curr):

            if i>=len(word) and curr.end_of_word:
                return True
            if i>=len(word) and not curr.end_of_word:
                return False

            if word[i]=='.':
                is_match = False
                for ch in range(0,26):
                    if chr(ch+97) not in curr.children:
                        continue

                    is_match = is_match or dfs(i+1,curr.children[chr(ch+97)])

                return is_match
                
            else:

                if word[i] not in curr.children:
                    return False
                return dfs(i+1,curr.children[word[i]])
            
            return False
            
        return dfs(0,curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
