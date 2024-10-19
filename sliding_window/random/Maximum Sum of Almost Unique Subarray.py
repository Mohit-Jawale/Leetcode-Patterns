class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        ### k -> subarray  = 4 ;  m = 3 
        ## [2,6,7,3,1,7]- 2,6,7,3 (18) -> 6,7,3,1 (17) -> 7,3,1,7(18)
        
        ### (2)
        ### [2,8,15,18,19,26]. 2n - >O(N)

        unique = Counter()
        left,right = 0 ,0


        prefixSum = 0
        max_sum = 0
    
        while right<len(nums):

            unique[nums[right]]+=1
            prefixSum+=nums[right]

            if right-left+1>k:
                unique[nums[left]]-=1
                if unique[nums[left]]==0:
                    del unique[nums[left]]
                prefixSum-=nums[left]
                left+=1
        
            if right-left+1==k and len(unique)>=m:
                max_sum = max(max_sum,prefixSum)
          
            right+=1

        return max_sum
        










