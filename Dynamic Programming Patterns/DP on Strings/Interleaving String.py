## dfs + memo
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        m = len(s1)
        n = len(s2)
        p = len(s3)

        if m+n<p:
            return False
        memo = {}
        

        def dfs(i,j,k):

            if i>=m and s3[k:]==s2[j:]:
                return True
            if j>=n and s3[k:]==s1[i:]:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            one, two, three = False,False,False

            if i<m and k<p and s1[i]==s3[k]:
                one = dfs(i+1,j,k+1)
            if j<n and k<p and s2[j]==s3[k]:
                two = dfs(i,j+1,k+1)
            

            memo[(i,j)] = one or two


            return one or two 
            

        return dfs(0,0,0)


            
            
            


        
