class TrieNode:
    def __init__(self):
        self.children = {}
        self.endChar = False
        self.suggestions= []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if len(curr.suggestions)<3:
                curr.suggestions.append(word)
        
        curr.endChar = True
    
    def search(self,word):
        curr = self.root
        res = []
        for c in word:
            if c not in curr.children:

                remaining = len(word)-len(res)
                for _ in range(remaining):
                    res.append([])
                break
            else:
                curr = curr.children[c]
                res.append(curr.suggestions)
        
        

        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trieobj = Trie()
        products.sort()
        for product in products:
            trieobj.insert(product)
        
        return trieobj.search(searchWord)
        

        
