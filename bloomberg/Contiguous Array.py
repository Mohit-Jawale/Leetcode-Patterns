class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        


        lookup = collections.defaultdict(int)
        ### key : subarray sum value: index

        prefixSum = 0

        lookup[0] = -1

        maxLen = 0


        for index,num in enumerate(nums):

            if num==0:
                prefixSum+= -1
            else:
                prefixSum+=1

            if prefixSum in lookup:
                maxLen = max(maxLen,index-lookup[prefixSum])
            else:
                lookup[prefixSum]=index ### this else is imp bcz that the longest and first
                ### occurence 
            
            

        return maxLen



