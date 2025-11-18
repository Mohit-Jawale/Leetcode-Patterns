
class TrieNode:
    def __init__(self):
        self.char = ""
        self.children = {}
        self.end_of_string = False

class MagicDictionary:

    def __init__(self):

        self.node = TrieNode()
        
    def insert_in_trie(self,word):
        curr = self.node

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.end_of_string = True



    def buildDict(self, dictionary: List[str]) -> None:

        for word in dictionary:
            self.insert_in_trie(word)


    def search(self, searchWord: str) -> bool:


        def dfs(curr,count,i):

            if count>1:
                return False
            
            if len(searchWord)==i:
                if count==1 and curr.end_of_string==True:
                    return True
                else:
                    return False
        
            for char,child in curr.children.items():
                
                newCount = count + (searchWord[i]!=char)
                
                if dfs(child,newCount,i+1):
                        return True
            
            return False
            
            

        return dfs(self.node,0,0)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
