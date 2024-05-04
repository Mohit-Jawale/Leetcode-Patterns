class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = -float('inf')
        stack = []

        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][1]>height:
                prevIdx,prevheight = stack.pop()
                maxArea = max(maxArea,abs(prevIdx-index)*prevheight)
                start = prevIdx ### to move the index backward

          
            stack.append((start,height))

        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))

        return maxArea   
