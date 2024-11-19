class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:



        lookup = collections.defaultdict(int)
        left,right = 0,0
        prefixSum = 0
        maxSum = 0


        while right<len(nums):

            if right-left+1<=k:
                prefixSum+=nums[right]
                lookup[nums[right]]+=1
                right+=1
            else:
                prefixSum-=nums[left]
                lookup[nums[left]]-=1
                if lookup[nums[left]]==0:
                    del lookup[nums[left]]
                left+=1
            
            if len(lookup)==k:
                maxSum = max(maxSum,prefixSum)
        
        return maxSum

          

 




     


        
