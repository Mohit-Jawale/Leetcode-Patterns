154. Find Minimum in Rotated Sorted Array IIclass Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ### for this problem thinking about the edge cases is critical
        left,right = 0,len(nums)-1

        while left<right:
            mid = left+(right-left)//2
            
            if nums[mid]==nums[right]:
                ####[10, 5, 10, 10, 10] -> just shrink by 1 
                if nums[mid]==nums[left]:
                    left+=1
                ###[1, 5, 10, 10, 10]  
                elif nums[mid]>nums[left]:
                    right = mid-1
                ###[20, 5, 10, 10, 10]
                else:
                    right = mid
            elif nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]

        
