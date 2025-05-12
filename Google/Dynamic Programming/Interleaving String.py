class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        memo = {}

        if len(s1)+len(s2)!=len(s3):
            return False


        def dfs(i,j,k):

            if k==len(s3) :
                return True

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

            if s1[i]==s3[k] and s2[j]==s3[k]:

                memo[(i,j)] =  dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
                return memo[(i,j)]

            if s1[i]==s3[k] and s2[j]!=s3[k]:
                memo[(i,j)] = dfs(i+1,j,k+1)
                return memo[(i,j)]
            
            if s2[j]==s3[k] and s1[i]!=s3[k]:
                memo[(i,j)] = dfs(i,j+1,k+1)
                return memo[(i,j)]

            
            return False


        return dfs(0,0,0)
        
