# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:


        ans = float('inf')
     
        def dfs(node):

            nonlocal ans
           
            if not node:
                return 

            if abs(node.val-target) < abs(ans-target):
                ans = node.val
            elif abs(node.val-target) == abs(ans-target):
                ans = min(node.val,ans)

            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        

        dfs(root)
        print(ans)
        return ans

            


            

            

            

        
