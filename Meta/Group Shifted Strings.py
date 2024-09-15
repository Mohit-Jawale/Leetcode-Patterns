class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:


        ### same length string can be grp together but not necessary
        ### How do I club them togther with some rule
        ### diff is nice rule abc -> all the char 1 
        ### if im able to find string which is same 
        ### mod 26 to handle circular logic az->
        
        
        #### step 1-:collection same length string togther
        
        groups = collections.defaultdict(list)

        for s in strings:
            pattern = ()

            for i in range(1,len(s)):
                pattern = pattern + ((ord(s[i]) - ord(s[i-1]) + 26) % 26,)
            
            groups[pattern].append(s)

        return groups.values()

        

