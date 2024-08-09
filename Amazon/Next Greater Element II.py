class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:


        monotonicStack = []

        ans = [-1]*len(nums)

        for i in range(0,2):

            for index,value in enumerate(nums):

                while monotonicStack and monotonicStack[-1][1]<value:
                    ans[monotonicStack.pop()[0]] = value
                
                monotonicStack.append((index,value))
        
        return ans
