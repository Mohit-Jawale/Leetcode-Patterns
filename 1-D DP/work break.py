#### dfs + memo
### This solution is reserved of how we implement dp is from the dict to s rather than s to wordict
###https://leetcode.com/problems/word-break/solutions/3766655/a-general-template-solution-for-dp-memoization/  
### refer this for dfs +memo solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        

        invaild = set()

        def dfs(s):

            nonlocal invaild

            if not s:
                return True
            if s in invaild:
                return False

            for w in wordDict:
                if (s.startswith(w) and dfs(s[len(w):])):
                    return True
            invaild.add(s)
            return False

        return dfs(s)  


### 1 DP

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]                
        
               



                

                


        
