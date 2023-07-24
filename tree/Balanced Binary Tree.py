# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = True
        flag = 0
        def dfs(node):
            nonlocal ans
            nonlocal flag
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            #### This flag technique is good if stuck in such sitution
            if abs(left-right)<=1 and flag==0:
                ans = True
            else:
                ans = False
                flag = 1    
            
            return max(left,right)+1

        dfs(root)
        return ans        
        
