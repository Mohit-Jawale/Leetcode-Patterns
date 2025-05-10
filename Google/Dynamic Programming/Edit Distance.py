class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        def dfs(i,j):
            ##### remeber this case
            if j>=len(word2):
                return len(word1)-i
            if i>=len(word1):
                return len(word2)-j
            
            same,notSame = float('inf'),float('inf')

            if word1[i]==word2[j]:
                same = dfs(i+1,j+1)
            else:
                delete_op = dfs(i+1,j)+1
                replace_op = dfs(i+1,j+1)+1
                insert_op = dfs(i,j+1)+1

                notSame = min(delete_op,replace_op,insert_op)

            return min(same,notSame)
        
        return dfs(0,0)


        
