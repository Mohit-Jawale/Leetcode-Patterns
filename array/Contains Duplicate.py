class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        lookup = {}

        for num in nums:
            if lookup.get(num):
                return True
            lookup[num] = 1    
        return False
