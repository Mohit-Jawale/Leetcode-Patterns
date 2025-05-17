# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        '''

        will it have negative number

        17
                4
            1       -3

        9       7


        '''
        max_path_sum = -float('inf')

        def dfs(node):

            nonlocal max_path_sum

            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            max_path_sum = max(max_path_sum,left_max+right_max+node.val)

            return max(max(left_max,right_max)+node.val,0)
        
        dfs(root)
        return max_path_sum
