class TrieNode:

    def __init__(self):

        self.children = {}
        self.end_of_word_index = -1

class Trie:

    def __init__(self):

        self.root = TrieNode()
    
    def insert(self,word:str,word_index:int)->None:

        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr = curr.children[char]
        
        curr.end_of_word_index = word_index
    
    def search(self,word:str)->int:

        curr = self.root

        for char in word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
            if curr.end_of_word_index>=0:
                return curr.end_of_word_index
        return -1



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        #### make trie of dict O(L+N) O(L+N)
        ### compare each word if it does nt exist or and shorter prefix exist store that in list

        Trie_obj = Trie()

        root_sentence = []

        for index,word in enumerate(dictionary):
            Trie_obj.insert(word,index)
        
        for word in sentence.split(' '):
            idx = Trie_obj.search(word)
            if idx!=-1:
                root_sentence.append(dictionary[idx])
            else:
                root_sentence.append(word)
        
        return " ".join(root_sentence)



        
