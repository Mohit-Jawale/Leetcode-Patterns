class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        prefixSum = 0
        total_subarray = 0

        for num in nums:

            prefixSum+=num
            prev_num = prefixSum%k
            if prev_num in lookup:
                total_subarray+=lookup[prev_num]
            
            lookup[prev_num]+=1
        
        return total_subarray

        
