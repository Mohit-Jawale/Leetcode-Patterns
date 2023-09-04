### dfs+memo
class Solution:
    def numDecodings(self, s: str) -> int:

        def isVaildCode(code):
            
            num = int(code)
            if len(code)!=len(str(num)):
                return False
            if 1<=num<=26:
                return True
            return False      

        count=0
        dp={}

        def dfs(k):

            nonlocal count,dp
            if k in dp:
                return dp[k]

            if k == len(s):
                return 1
            
            for i in range(k,len(s)):
                nextCode = s[k:i+1]
                if isVaildCode(nextCode):
                    count+=dfs(i+1)                  
                else:
                    break    
 
            dp[k]=count
            return count

        return dfs(0)





##### 1D dp

class Solution:
    def numDecodings(self, s: str) -> int:

        def isVaildCode(code):
            
            num = int(code)
            if len(code)!=len(str(num)):
                return False
            if 1<=num<=26:
                return True
            return False      

        n = len(s)
        dp=[0]*(n+1)
        dp[n] = 1

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                dp[i]=dp[i+1]
                if i<n-1 and isVaildCode(s[i:i+2]):
                    dp[i]+=dp[i+2]

        return dp[0]               
