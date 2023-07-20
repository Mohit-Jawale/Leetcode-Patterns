class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}

        for index,num in enumerate(nums):
            check = target-num
            if check in lookup:
                return [lookup[check],index]
            lookup[num] = index



        
        
