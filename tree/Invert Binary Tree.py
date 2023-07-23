# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        def dfs(node):
            if not node:
                return

            right = dfs(node.left)
            left = dfs(node.right)
            node.right = right
            node.left = left

            return node

        return dfs(root)    

                
        
