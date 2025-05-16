# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        LCA in BST
        compare the p and q val and expoilt the BSt property

        '''


        def dfs(node):
            if not node:
                return None
            if p.val==node.val or q.val==node.val:
                return node
            if (p.val<node.val and q.val>node.val) or (p.val>node.val and q.val<node.val):
                return node
            
            if p.val<node.val and q.val<node.val:
                return dfs(node.left)
            
            if p.val>node.val and q.val>node.val:
                return dfs(node.right)
        
        return dfs(root)
            
        
