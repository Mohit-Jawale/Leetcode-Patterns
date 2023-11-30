class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(subarraySum):
            total = 0
            mink=1

            for num in nums:
                total+=num
                if total>subarraySum:
                    total = num
                    mink+=1
                    if mink>k:
                        return False

            return True            


        left, right = max(nums),sum(nums)

        while left<right:
            mid = left+(right-left)//2

            if feasible(mid):
                right=mid
            else:
                left = mid+1

        return left            
