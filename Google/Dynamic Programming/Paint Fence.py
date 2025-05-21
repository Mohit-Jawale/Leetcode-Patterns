class Solution:
    def numWays(self, n: int, k: int) -> int:

        '''
        total no of ways to paint the fence find all ways
        

        conditions:
        - unique color for post k=2
        - no three or more post with same clor k= 3^7

        n = 7 k = 3
        |R |R |G |G |R
        | 3|3 |2 | | | | |

        '''
        memo = {}

        def dfs(n):

            if n==1:
                return k
            if n==2:
                return k*k
            if n in memo:
                return memo[n]
            
            res = (k-1)*(dfs(n-1)+dfs(n-2)) #### how many valid choice I have for each option

            memo[n] = res

            return res
        
        return dfs(n)
        
