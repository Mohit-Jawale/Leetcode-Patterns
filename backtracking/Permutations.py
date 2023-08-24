class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(permutation):

            nonlocal ans
            if len(permutation) == len(nums):
                ans.append(permutation)
                return

            for num in nums:
                if num not in permutation:
                    temp = permutation + [num]
                    dfs(temp)


        dfs([])
        return ans            
