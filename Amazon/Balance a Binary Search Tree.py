# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        inorder = []

        def dfs(node):

            nonlocal inorder
            if not node:
                return
        
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        

        dfs(root)

        def build(l,r):

            if l==r:
                return None

            mid = l+(r-l)//2

            node = TreeNode(inorder[mid])
            node.left = build(l,mid)
            node.right  = build(mid+1,r)

            return node
        

        return build(0,len(inorder))
        
