class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:


        lookup = collections.defaultdict(int)
        lookup[0] = -1 ### this is index

        prefix_sum = 0
        max_length_subarray = 0

        for index,num in enumerate(nums):

            prefix_sum+=num

            prev_sum = prefix_sum-k

            if prev_sum in lookup:
                curr_length_subarray = index-lookup[prev_sum] #### its not +1 bcz we are not taking the value after the index
                max_length_subarray = max(max_length_subarray,curr_length_subarray)

            if prefix_sum not in lookup:
                lookup[prefix_sum]=index

        return max_length_subarray

                
        
