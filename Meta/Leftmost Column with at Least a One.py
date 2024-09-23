# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        row,col = binaryMatrix.dimensions()
        min_col = col
      

        for i in range(row):

            left,right = 0,col

            while left<right:
                
                mid = left+(right-left)//2

                if binaryMatrix.get(i,mid)==1:
                    right = mid
                else:
                    left = mid+1
            
            min_col = min(left,min_col)

        return min_col if min_col<col else -1
            

        



        

        
