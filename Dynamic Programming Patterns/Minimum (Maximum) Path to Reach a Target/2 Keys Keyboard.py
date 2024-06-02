
class Solution:
    def minSteps(self, n: int) -> int:

        memo = {}
        def dfs(i,copied):

            if i==n:
                return 0
            if i>n:
                return float('inf')

            if (i,copied) in memo:
                return memo[(i,copied)]
            
            copyAll = float('inf')
            if i != copied:
                copyAll = dfs(i,i)+1
            
            paste = float('inf')
            if copied>0:
                paste = dfs(i+copied,copied)+1

            minSteps= min(copyAll,paste)

            memo[(i,copied)] = minSteps

            return minSteps


        return dfs(1,0)
# class Solution:
#     def minSteps(self, n: int) -> int:
        
#         visited = set()

#         def dfs(store,display):
      
#             if len(display)==n:
#                 return 0
                
#             if len(display)>n:
#                 return float('inf')   

#             if (store,display) in visited:
#                 return float('inf')
#             else:
#                 visited.add((store,display))         
            

#             copyAll = dfs(display,display) + 1

#             pasteAll = dfs(store,display+store) + 1

#             minOp = min(copyAll,pasteAll)

#             return minOp

#         return dfs('','A')    
