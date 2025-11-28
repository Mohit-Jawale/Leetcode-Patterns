class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left,right = 0, len(arr)-1

        while left<=right:

            mid = left + (right-left)//2

            if arr[mid]-mid-1<k:
                left = mid+1
            else:
                right = mid-1
        ### left this the total number in the arr which are less than k present in the arr
        ### to find the kth missing number add k to left
        return left+k
        
