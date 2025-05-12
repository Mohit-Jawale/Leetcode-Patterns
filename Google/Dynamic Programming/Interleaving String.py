class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        memo = {}


        def dfs(i,j,k):

            if i>=len(s1):
                if s2[j:]==s3[k:]:
                    return True
                else:
                    return False
            
            if j>=len(s2):
                if s1[i:]==s3[k:]:
                    return True
                else:
                    return False

            if (i,j) in memo:
                return memo[(i,j)]

            one,two = False,False

            if i<len(s1) and k<len(s3) and s1[i]==s3[k] :
                one = memo[(i,j)] = dfs(i+1,j,k+1)
                
            
            if j<len(s2) and k<len(s3) and s2[j]==s3[k]:
                two = dfs(i,j+1,k+1)
                
            memo[(i,j)] = one or two
            
            return memo[(i,j)]


        return dfs(0,0,0)
        
