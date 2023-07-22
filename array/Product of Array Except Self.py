### This question has a lot of things going on in it.
### using deque
### What are prefix and suffix

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        prefix.append(1)

        suffix = collections.deque()
        suffix_num = 1
        suffix.append(suffix_num)



        for i in range(len(nums)-1):### why till -1? bcz we are calculating ahead
            prefix.append(nums[i]*prefix[i])

        for i in range(len(nums)-1,0,-1): ### same for this
            suffix_num = suffix_num * nums[i]
            suffix.appendleft(suffix_num)

        for i in range(0,len(prefix)):
            prefix[i] = prefix[i]*suffix[i]

        return prefix
        
