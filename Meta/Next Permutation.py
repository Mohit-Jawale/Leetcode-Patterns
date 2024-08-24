class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### just remeber the algorithm for Meta or Amazon

        pivot = 0   

        ### find pivot

        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pivot = i-1
                break
        else:
            nums.reverse()
            return
        
        ### first number greater from right which can be swapped with pivot
        ### bcz if I go from right and put that num in front that number will be the greatest
        swap = len(nums)-1

        while nums[swap]<=nums[pivot]:
            swap-=1

        nums[swap],nums[pivot] = nums[pivot],nums[swap]

        nums[pivot+1:] = reversed(nums[pivot+1:])

        return


        





        
