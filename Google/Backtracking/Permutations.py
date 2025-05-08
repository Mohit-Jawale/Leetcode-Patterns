class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []


        def get_all_permutations(combination):


            if len(combination)==len(nums):
                ans.append(combination[:])
                return
            
            for k in range(0,len(nums)):

                if nums[k] in combination:
                    continue

                combination.append(nums[k])

                get_all_permutations(combination)

                combination.pop()

        get_all_permutations([])
        return ans
        
