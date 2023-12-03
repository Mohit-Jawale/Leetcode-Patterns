class Solution:
    def minSteps(self, n: int) -> int:
        
        visited = set()

        def dfs(store,display):
      
            if len(display)==n:
                return 0
                
            if len(display)>n:
                return float('inf')   

            if (store,display) in visited:
                return float('inf')
            else:
                visited.add((store,display))         
            

            copyAll = dfs(display,display) + 1

            pasteAll = dfs(store,display+store) + 1

            minOp = min(copyAll,pasteAll)

            return minOp

        return dfs('','A')    
