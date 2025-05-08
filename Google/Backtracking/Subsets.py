class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # [1,2,3]
            # ^
        ########     []
        ####.   [1]          [2].        [3]

        ####[1,2]  [1,3].      [2,3]

        ####[1,2,3]
        ans = []


        def dfs(i,subset):


            if i>len(nums):
                return
            
            ans.append(subset[:]) #### remember this is to save the current state its like preorder
            
            for k in range(i,len(nums)):

                subset.append(nums[k])
                dfs(k+1,subset)
                subset.pop()

        dfs(0,[])
        return ans



        
