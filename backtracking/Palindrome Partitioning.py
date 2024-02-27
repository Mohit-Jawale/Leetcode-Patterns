### this problem is different from other backtracking problems so look carefully how the tree is made
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        partitions= []
        substring = []

        def dfs(s,substring):

            if len(s)==0:
                partitions.append(copy.deepcopy(substring))
                return

            for k in range(len(s)):
                substring.append(s[:k+1])
                if substring[-1]==substring[-1][::-1]:
                    dfs(s[k+1:],substring)
                substring.pop()

        
        dfs(s,substring)
        return partitions



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []

        def dfs(k,substrings):

            if k ==len(s):
                ans.append(substrings.copy())
                return

            for i in range(k,len(s)):
                substring = s[k:i+1]
                if substring == substring[::-1]:

                    substrings = substrings + [substring]
                    dfs(i+1,substrings)
                    substrings.pop()
                    

        dfs(0,[])
        return ans        
        
