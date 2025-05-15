# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        '''
        dfs 


        '''

        def preorder_dfs(node,total):

            if not node:
                return False
            
            if total+node.val == targetSum and not node.left and not node.right:
                return True
            

            left = preorder_dfs(node.left,total+node.val)
            right = preorder_dfs(node.right,total+node.val)

            return left or right
        
        return preorder_dfs(root,0)


            
        
