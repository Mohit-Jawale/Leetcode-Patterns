## This problem has some extra thinking for calculating max bcz we dont want to add the negative value to our max_path. thats why we have
#### find out max at left and right return 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = float('-inf')

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            max_path = max(left+right+node.val,max_path) 

            return  node.val + max(left,right)

        dfs(root)
        return max_path    



        
