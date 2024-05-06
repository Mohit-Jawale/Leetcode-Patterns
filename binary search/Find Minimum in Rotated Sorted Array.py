class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left,right = 0,len(nums)-1

        while left<right:
            mid = left+(right-left)//2

            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right = mid ### for if they are equal or its on the left side
        

        return nums[left]
        

# class Solution:
#     def findMin(self, nums: List[int]) -> int:

#         left, right = 0,len(nums)-1
#         middle = 0
#         ### to check if its already sorted or make sure its equal to for if there are only one element in the array
#         if nums[left]<=nums[right]:
#             return nums[left]

#         while left<=right:

#             middle = (left+right)//2
#             ### This condition make sure that we found our breaking point or two sorted arrays
#             if nums[middle]>nums[middle+1]:
#                 break
#             else:

#                 if nums[left] > nums[middle]:
#                     right = middle-1
#                 else: 
#                     left = middle+1
                  
      
#         return nums[middle+1]                    

