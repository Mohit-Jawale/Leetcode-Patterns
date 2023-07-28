class Solution:
    def maxArea(self, height: List[int]) -> int:

        left,right = 0 ,len(height)-1

        max_area = float("-inf")

        while left < right:
            if height[left]<height[right]:
                max_area = max(max_area,height[left]*(right-left))
                left+=1
            else:
                max_area = max(max_area,height[right]*(right-left))
                right-=1
        
        return max_area

        
