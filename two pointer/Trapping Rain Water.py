#### min(l,r)-height is the key and then you apply two pointer technique

class Solution:
    def trap(self, height: List[int]) -> int:

        left,right = 0,len(height)-1
        leftMax, rightMax = height[left],height[right]
        res=0

        while left<right:
            
            if leftMax<rightMax: ### why move left when rightmax is grt bcz imagine [1,0,2] here if we move right we dont know if there is grt vaalue to left to give min height
                left+=1
                leftMax = max(leftMax,height[left])
                res += leftMax-height[left]
            else:
                right-=1
                rightMax = max(rightMax,height[right])
                res += rightMax-height[right]

        return res            

        
