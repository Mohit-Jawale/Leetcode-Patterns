class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        group_anagrams = collections.defaultdict(list)

        for word in strs:
            count = [0]*26

            for w in word:
                count[ord(w)-ord('a')]+=1
            group_anagrams[tuple(count)].append(word) 
           
        return group_anagrams.values()    
        
