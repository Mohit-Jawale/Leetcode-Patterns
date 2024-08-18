class Solution:
    def validStrings(self, n: int) -> List[str]:

        ans = []


        def dfs(currString):

            nonlocal ans

            if len(currString) == n:
                ans.append(copy.deepcopy(currString))
                return

            dfs(currString+"1")

            if not currString or currString[-1]!="0":
                 dfs(currString+"0")
        

        dfs("")
        return ans

