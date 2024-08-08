class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        monotonicDecreasingStack = []
        nextgreater = [-1]*len(nums2)
        hashmap = {}
        ans = []
        for index,value in enumerate(nums2):
            hashmap[value] = index
            while monotonicDecreasingStack and monotonicDecreasingStack[-1][1]<value:
                i,j = monotonicDecreasingStack.pop()
                nextgreater[i] = value
            else:
                monotonicDecreasingStack.append((index,value))

        for i in nums1:
            ans.append(nextgreater[hashmap[i]])
        
        return ans
