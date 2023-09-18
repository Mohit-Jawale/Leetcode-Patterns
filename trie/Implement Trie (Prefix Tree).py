### just remember the why we are using endofword
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.EndOfWord = True
  

    def search(self, word: str) -> bool:

        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.EndOfWord          

    def startsWith(self, prefix: str) -> bool:
         
         curr = self.root
         for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
         return True   

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
