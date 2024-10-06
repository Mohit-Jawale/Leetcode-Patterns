class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        ## [3,1,4,2]- >> p=6
        ### 
        ### 



        total = sum(nums)
        target = total%p
    
        if target==0:
            return 0
        if total<p:
            return -1

        
        lookup = {0:-1}
        prefixSum = 0
        minLen =  len(nums)

        for index,num in enumerate(nums):

            prefixSum+=num
            print(lookup,prefixSum,target)

        
            if (prefixSum-target+p)%p in lookup:
                minLen = min(minLen,index-lookup[(prefixSum-target+p)%p])
            
            if prefixSum not in lookup:
                lookup[prefixSum%p] = index
                
            
    
        return minLen if minLen!=len(nums) else -1

            





         


        
        
