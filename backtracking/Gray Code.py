class Solution:
    def grayCode(self, n: int) -> List[int]:


        visited = set()
        grayCode = [0]
        visited.add(0)

        def dfs(i,grayCode):
        
     
            if len(grayCode)==pow(2,n):
                return True

            for k in range(0,n):

                num_flipped = i ^ (1 << k)
          
                if num_flipped in visited:
                    continue

                visited.add(num_flipped)
                grayCode.append(num_flipped)

                if dfs(num_flipped,grayCode):
                    return grayCode

                visited.remove(num_flipped)
                grayCode.pop(num_flipped)
        
        return dfs(0,grayCode)
        


                
                






            


            


            



            
        
