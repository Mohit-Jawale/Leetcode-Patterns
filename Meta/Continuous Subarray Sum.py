class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        ### o(n^2) - wont worry
        ### good array is at least two and sum of subarrary multiple of k


        currSum = 0

        diffHash = {}

        for index,value in enumerate(nums):

            currSum+=value

            if currSum%k==0 and (index+1)>=2:
                return True

            if currSum%k not in diffHash:
                diffHash[currSum%k] = index

            elif currSum%k in diffHash:
                windowlen = index-diffHash[currSum%k]
                if windowlen>=2:
                    return True
            

        return False
                
            
            




        
        



        
