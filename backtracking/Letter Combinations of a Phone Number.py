class Solution:
    def letterCombinations(self, digits: str) -> List[str]:



        mapping = {

            2:"abc",
            3:'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9:'wxyz'

        }

        ans = []

        def dfs(k,combination):

            if k==len(digits):
                ans.append("".join(combination))
                return

            alpha = mapping[int(digits[k])]

            for i in alpha:

                dfs(k+1,combination + [i])

        dfs(0,[])
        return ans if len(digits)!=0 else []
        
        
