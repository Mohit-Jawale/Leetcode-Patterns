class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:


        stack = []

        for index,height in enumerate(heights):
            
            if not stack:
                stack.append((height,index))
            elif stack[-1][0]>height:
                stack.append((height,index))
            else:
                while stack and stack[-1][0]<=height:
                    stack.pop()
                stack.append((height,index))
        
        ans = []
        for h,v in stack:
            ans.append(v)
        return ans




        
