# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dfs(node):

            nonlocal ans

            if not node:
                return 0,True,float('inf'),-float('inf')
            
            sumLeft,left,minLeft,maxLeft = dfs(node.left)
            sumRight,right,minRight,maxRight = dfs(node.right)

            if left and right and maxLeft<node.val<minRight:
                ans = max(sumLeft+sumRight+node.val,ans)
                return sumLeft+sumRight+node.val,True,min(minLeft,node.val),max(maxRight,node.val)
            return 0,False,float('inf'),-float('inf')
        
        dfs(root)
        return ans
                

        
