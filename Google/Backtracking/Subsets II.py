class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #### all possibe backtracking using dfs type of algo

        ##### [1,2,2]

        
        ####.       []
        #### [1].       [2].    [2]
        ###[1,2] .  [2,2]
        ####[1,2,2]

        nums.sort()
        ans = []

        def dfs(i,subset):

            if i>len(nums):
                return 
            
            ans.append(subset[:])

            for k in range(i,len(nums)):

                if k>i and nums[k-1]==nums[k]: #### here remember the k>i not k>0 why bcz at every level we want to skip first element i.e zeroth index
                    continue
                
                subset.append(nums[k])
                dfs(k+1,subset)
                subset.pop()

        dfs(0,[])
        return ans


        
