### need to rememeber the trick to transerve the 2-d matrix as 1-D matrix using only column


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n-1


        while left<=right:

            middle = (left+right)//2

            if matrix[middle//n][middle%n] == target:
                return True
            else:
                if matrix[middle//n][middle%n] < target:
                    left = middle+1
                else:
                    right = middle-1

        return False                   


        
