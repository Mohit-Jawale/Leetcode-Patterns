class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        nums.sort()
        closest = float('inf')

        for index in range(len(nums)):

            left,right = index+1,len(nums)-1

            while left<right:

                current_sum = nums[index] + nums[left] + nums[right]

                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                if current_sum>target:
                    right-=1
                elif current_sum<target:
                    left+=1
                else:
                    return closest

        return closest
            





        
