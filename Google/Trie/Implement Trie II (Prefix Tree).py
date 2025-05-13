class TrieNode:

    def __init__(self):
        self.children = {}
        self.total_word_end = 0
        self.total_char = 0



class Trie:

    def __init__(self):

        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root

        for char in word:

            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.total_char+=1

        curr.total_word_end+=1
        

    def countWordsEqualTo(self, word: str) -> int:

        curr = self.root

        for char in word:

            if char not in curr.children:
                return 0
            curr = curr.children[char]

        return curr.total_word_end
            
        

    def countWordsStartingWith(self, prefix: str) -> int:

        curr = self.root

        for char in prefix:

            if char not in curr.children:
                return 0
        
            curr = curr.children[char]
            
        return curr.total_char

        

    def erase(self, word: str) -> None:
        curr = self.root

        for char in word:

            if char not in curr.children:
                return 0
            
            curr = curr.children[char]
            curr.total_char-=1
            
        curr.total_word_end-=1

        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
