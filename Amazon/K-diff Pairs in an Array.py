class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:


        # pairs = set()
        # nums.sort()

        # for index,value in enumerate(nums):

        #     for i in range(index+1,len(nums)):
        #         if abs(value-nums[i])==k:
        #             pairs.add((value,nums[i]))
        
        # return len(pairs)

        pairCount = 0

        counter = Counter(nums)

        for x in counter:

            if k>0 and x+k in counter:
                pairCount+=1
            elif k==0 and counter[x]>1:
                pairCount+=1
        
        return pairCount
            





        
