# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        left,right = 0,pow(10,4)-1
        INVALID = pow(2,31)-1

        while left<=right:

            mid = (left+right)//2

            value = reader.get(mid)

            if value == INVALID:
                right = mid-1
            else:
                if value==target:
                    return mid
                else:
                    if value<target:
                        left = mid+1
                    else:
                        right = mid-1
        
        return -1
                
                
            




        
