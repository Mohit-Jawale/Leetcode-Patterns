class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        lookup = collections.defaultdict(int)
        lookup[0]=1 ### key:total odd count yet , value : count
        count = 0

        odd = 0

        for num in nums:

            print(lookup)
            if num%2!=0:
                odd+=1

            prev_odd_count = odd-k
            if prev_odd_count in lookup:
                count+=lookup[prev_odd_count]
            
            lookup[odd]+=1
            

        return count



        
