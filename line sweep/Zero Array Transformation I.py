class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)

        diff_arr = [0]*(n+1)

        for s,e in queries:

            diff_arr[s]+=1
            diff_arr[e+1]-=1
        
        if not diff_arr[0]>=nums[0]:
            return False

        for i in range(1,len(nums)):

            diff_arr[i]+=diff_arr[i-1]
            if diff_arr[i]<nums[i]:
                return False
        
        return True

        






        
        

        
