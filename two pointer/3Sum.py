class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        nums.sort()
        res = []

        for index,target in enumerate(nums):
            
            if target>0:
                break

            if index>0 and nums[index]==nums[index-1]:
                continue
            
            left,right = index+1,len(nums)-1
   
         
            while left<right:
                if nums[left]+nums[right]<-target:
                    left+=1
                elif nums[left]+nums[right]>-target:
                    right-=1
                else:
                    res.append([nums[left],nums[right],target])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1


        return res 

