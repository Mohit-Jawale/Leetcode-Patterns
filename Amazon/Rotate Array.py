class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        k = k%(len(nums))

        def reverseTillK(left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        
        n = len(nums)

        reverseTillK(0,n-1)
        reverseTillK(0,k-1)
        reverseTillK(k,n-1)



        
