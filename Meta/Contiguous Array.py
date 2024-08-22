class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        


        ### Note Sliding window technique cant be applied to this bcz the valid window cant
        #### be determine

        diffindex = {}
        zeros,ones = 0,0
        maxLength = 0


        for index,value in enumerate(nums):

            if value == 0:
                zeros+=1
            else:
                ones +=1
            
            if ones-zeros not in diffindex:
                diffindex[ones-zeros]=index

            if ones == zeros:
                maxLength = ones+zeros
            else:
                maxLength = max(maxLength,index-diffindex[ones-zeros])
                
        return maxLength






