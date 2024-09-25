class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        longest_s = 0

        res = set()

        def dfs(curr_index,curr_res,left,right):

            nonlocal longest_s,res

            if curr_index>=len(s):
                
                if left==right:
                    if longest_s<len(curr_res):
                        longest_s = len(curr_res)
                        res = set()
                        res.add("".join(curr_res))
                    elif longest_s==len(curr_res):
                        res.add("".join(curr_res))
                
                return


            curr_char = s[curr_index]

            if curr_char =='(':

                dfs(curr_index+1,curr_res+[curr_char],left+1,right)

                dfs(curr_index+1,curr_res,left,right)
            
            elif curr_char ==')':

                if left>right:
                    dfs(curr_index+1,curr_res+[curr_char],left,right+1)
                
                dfs(curr_index+1,curr_res,left,right)
            else:
                dfs(curr_index+1,curr_res+[curr_char],left,right)
        
        dfs(0,[],0,0)
        return res
                



               


        
