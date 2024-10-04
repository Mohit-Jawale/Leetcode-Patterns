### amazing 

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        res = []

        def dfs(curr_idx,curr_res,curr_sum,prev):
     
            if curr_idx>=len(num):

                if curr_sum==target:
                    res.append("".join(curr_res))
                return
            
            else:

                for i in range(curr_idx,len(num)):
                    
                    curr_str = num[curr_idx:i+1]
                    curr_num = int(curr_str)


                    if not curr_res:
                        dfs(i+1,[curr_str],curr_num,curr_num)
                    else:
                        dfs(i+1,curr_res+['+']+[curr_str], curr_sum+curr_num, curr_num)
                        dfs(i+1,curr_res+['-']+[curr_str], curr_sum-curr_num, -curr_num)
                        dfs(i+1,curr_res+['*']+[curr_str], curr_sum-prev + prev*curr_num, prev*curr_num)
        
                    if curr_num == 0:
                        break


        dfs(0,[],0,0)
        return res
