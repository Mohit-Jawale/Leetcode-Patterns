class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        lookup = collections.defaultdict(int)

        lookup[0] = 1 ###3 this is base case [1,1,1,1,1,1] k=3 so here at i=2 we will have 1 arr with sum 0 previously
        prefixSum = 0
        res = 0

        for i in nums:
            prefixSum+=i
            curr_sum = prefixSum - k
            if curr_sum in lookup:
                res+=lookup[curr_sum]
            lookup[prefixSum]+=1
        
        return res


        
