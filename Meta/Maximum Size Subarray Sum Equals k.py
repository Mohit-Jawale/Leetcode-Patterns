class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        ### [1,0,5,3,6]  k=3
        ### 3-3=0
        ### [3,5,8] = 16-13 = 3
        ###lookup = [sum:index]


        lookup = {0:-1}

        prefixSum = 0
        res = 0

        for index,num in enumerate(nums):

            prefixSum+=num

            if prefixSum-k in lookup:
                res = max(res,index-lookup[prefixSum-k])
                
            if prefixSum not in lookup:
                lookup[prefixSum]=index
        
        return res


        
        
