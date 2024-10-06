class TrieNode:

    def __init__ (self):
        self.children = {}
        self.endOfNum = False

class Trie:

    def __init__ (self):
        self.root = TrieNode()
    

    def insert(self,num):

        char_num = str(num)
        curr = self.root

        for char in char_num:
            if char not in curr.children:
                curr.children[char]= TrieNode()
            curr = curr.children[char]
        curr.endOfNum = True


    def search(self,num):

        char_num = str(num)
        curr = self.root
        count = 0

        for char in char_num:
            if char not in curr.children:
                return count
            curr = curr.children[char]
            count+=1
        
        return count



class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:


        t  = Trie()

        ##O(m+n)
        for num in arr1:
            t.insert(num)

        max_len = 0
        for num in arr2:
            max_len = max(t.search(num),max_len)

        return max_len
        


        

            



        
