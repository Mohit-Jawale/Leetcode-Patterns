https://www.youtube.com/watch?v=0d6WF79hQMEimport heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:


        def less_than_k(target):

            count = 0

            for row in range(len(matrix)):

                count+=bisect_right(matrix[row],target)
            
            return count


        left,right = matrix[0][0],matrix[-1][-1]


        while left<right:

            mid = left+(right-left)//2

            if less_than_k(mid) < k:
                left = mid+1
            else:
                right = mid
        
        return left
        
        
        
          
