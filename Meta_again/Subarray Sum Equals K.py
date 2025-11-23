class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0]=1
        ans = 0
        for curr_num in nums:

            prefix_sum+=curr_num

            if prefix_sum-k in lookup:
                ans+=lookup[(prefix_sum-k)]
            
            lookup[prefix_sum]+=1
        
        return ans


        
        
