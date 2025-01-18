
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        
 
        # memo = {}

        # def dfs(i,valid_ss):
         
        #     if len(valid_ss)==4:
        #         if nums[valid_ss[0]]*nums[valid_ss[2]] == nums[valid_ss[1]]*nums[valid_ss[3]]:
        #             return 1
        #         return 0

        #     if i>=len(nums):
        #         return 0
            
        #     total = 0
        #     for k in range(i,len(nums)):

        #         total+=dfs(k+2,valid_ss+[k])
            
            
        #     return total
        
        # return dfs(0,[])

        ratios = collections.defaultdict(list)

        for p in range(0,len(nums)):
            for q in range(p+2,len(nums)):
                ratios[(nums[p]/nums[q])].append(q)
        

        for key,value in ratios.items():
            ratios[key] = list(sorted(value))
        
        ans = 0

        for r in range(4,len(nums)):
            for s in range(r+2,len(nums)):
                ratio = nums[s]/nums[r]

                if ratio in ratios:

                    left,right = 0, len(ratios[ratio])-1

                    while left<=right:

                        mid = (left+right)//2
                        q = ratios[ratio][mid]

                        if q > r-2:
                            right = mid-1
                        else:
                            left = mid+1
                    
                    ans+=left
        
        return ans
                
