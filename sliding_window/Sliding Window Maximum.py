class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        deque = collections.deque()
        ans = []

        l = r = 0

        while r < len(nums):
            #### putting index in deque rather than nums for checking the left condition is smart idea
            while deque and not nums[deque[-1]]>nums[r]:
                deque.pop()

            deque.append(r)
          
            ### As we will be using monotonic decreasing deque the left index at the start will be always equal to window if not we have to popfrom left
            ### becasue its always decreasing the new index in the window will be greater we need to remove the older one
            if l > deque[0]:
                deque.popleft()

        
            if r+1>=k:
                ans.append(nums[deque[0]])
                l+=1

            r+=1
        return ans        


        
