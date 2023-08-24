class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        visited =set()
        ans = []
        ans.append([])
        nums.sort()

        def dfs(subset,k):

            if k==len(nums):
                return

            for num in nums[k:]:
                temp = subset+[num]
                if tuple(temp) in visited:
                    k+=1
                    continue
                ans.append(temp)    
                visited.add(tuple(temp))    
                dfs(temp,k+1)
                k+=1


        dfs([],0)
        return ans

        
