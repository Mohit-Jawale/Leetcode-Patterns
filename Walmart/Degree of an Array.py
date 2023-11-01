class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        counter = Counter(nums)
        highestFreq = max(counter.values())
        freqCounter = Counter()
        left,right = 0 , 0
        count = 1
        ans = len(nums)
        while right<len(nums):
            freqCounter[nums[right]]+=1
            while freqCounter[nums[right]]==highestFreq:
                ans = min(right-left+1,ans)
                freqCounter[nums[left]]-=1
                left+=1
            right+=1

        return ans            
            
        
