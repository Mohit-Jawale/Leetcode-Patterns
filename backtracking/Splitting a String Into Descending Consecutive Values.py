class Solution:
    def splitString(self, s: str) -> bool:

        n = len(s)

        def dfs(i,prestring):

            if i==n and len(prestring)>=2:
                return True
            if i>=n:
                return False
            
            for k in range(i,n):
                curr_value = int(s[i:k+1])

                if prestring and prestring[-1]-curr_value!=1:
                    continue

                prestring.append(curr_value)
                if dfs(k+1,prestring):
                    return True
                prestring.pop()
            
            return False
            

        return dfs(0,[])

        
