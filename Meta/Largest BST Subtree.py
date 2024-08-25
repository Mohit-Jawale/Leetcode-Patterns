# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#### beautiful quesion 
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:


        if not root:
            return 0
        
        maxCount = 1


        def dfs(node,leftMax,rightMax):

            nonlocal maxCount

            if not node:
                return (False,-float('inf'),float('inf'),0)

            if not node.left and not node.right:
                return (True,node.val,node.val,1)
            

            isBSTleft,lmin,lmax,lcount = dfs(node.left,leftMax,rightMax)
            isBSTright,rmin,rmax,rcount = dfs(node.right,leftMax,rightMax)


            if isBSTleft and isBSTright and lmax<node.val<rmin:
                curr_len = 1+lcount+rcount
                maxCount = max(curr_len,maxCount)
                return (True,lmin,rmax,curr_len)

            elif isBSTleft and not node.right and lmax<node.val:
                curr_len = 1+lcount
                maxCount = max(curr_len,maxCount)
                return (True,lmin,node.val,curr_len)
            
            elif isBSTright and not node.left and node.val<rmin:
                curr_len = 1+rcount
                maxCount = max(curr_len,maxCount)
                return (True,node.val,rmax,curr_len)
            else:
                return (False,-float('inf'),float('inf'),0)
            
        

        dfs(root,-float('inf'),float('inf'))
        return maxCount
