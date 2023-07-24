# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None
        def dfs(node):
            
            nonlocal lca
            if not node:
                return

            if p.val<node.val and q.val<node.val:
                dfs(node.left)
            elif p.val>node.val and q.val>node.val:
                dfs(node.right)
            else:
                lca = node
                return

                  
        dfs(root)
        return lca
        
