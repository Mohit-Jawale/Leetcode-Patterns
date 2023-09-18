class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndofWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr = curr.children[w]
        curr.EndofWord = True           

    def search(self, word: str) -> bool:
 

        def dfs(node,index):
            if index == len(word):
                return node.EndofWord

            if word[index]=='.':
                for w in node.children.values():
                    if dfs(w,index+1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]],index+1)

            return False

        return dfs(self.root,0)    



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
