# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        rightSum = 0

        def dfs(node):

            nonlocal rightSum

            if not node:
                return 0

            dfs(node.right)
            node.val += rightSum
            rightSum = node.val
            dfs(node.left)

    
        dfs(root)
        return root
        
