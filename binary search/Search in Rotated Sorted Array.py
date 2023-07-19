class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def detect_rotation(left,right):

            if nums[left]<=nums[right]:
                return left

            middle = 0
            while left<=right:

                middle = (left+right)//2

                if nums[middle]>nums[middle+1]:
                    break
                else:
                    if nums[left] < nums[middle]:
                        left = middle+1
                    else:
                        right = middle-1

            return middle+1

        def binary_search(left,right,target):

            while left<=right:

                middle = (left+right)//2

                if  nums[middle]==target:
                    return middle
                else:
                    if nums[middle] >= target:
                        right = middle-1
                    else:
                        left = middle+1

            return -1           

        left, right = 0, len(nums)-1
        pivot = detect_rotation(left,right)
        print(pivot)

        if nums[left]<=nums[right]:
            return binary_search(left,right,target)
        #### compare with target why? bcz if target is grter than or equal left it will lie in left side of pivot  else its on right
        elif nums[left]<=target:
            return binary_search(left,pivot,target)
        else:
            return binary_search(pivot,right,target)     



        
