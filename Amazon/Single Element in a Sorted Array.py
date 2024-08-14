class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:


        #### 1,1,4,4,5 ->>> odd length mid == mid+1 move left = mid+1
                  
        #### 1,2,2,6,6 ->>> odd mid == mid-1

        ### if its different then thats the ans mid == mid+1

        ### the length will always be odd



        left,right = 0,len(nums)-1

        while left<=right:

            mid = left+(right-left)//2

            if(mid-1<0 or nums[mid-1]!=nums[mid]) and (mid+1 == len(nums) or  nums[mid+1]!=nums[mid]):
                return nums[mid]

            leftSize = 0
            if nums[mid-1]==nums[mid]:
                leftSize= mid-1
            else:
                leftSize = mid

            if leftSize%2:
                right = mid-1
            else:
                left = mid+1

        return -1
