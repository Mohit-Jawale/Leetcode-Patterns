# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        def dfs(node):

            nonlocal depth
            if not node:
                return 1

            depth = max(dfs(node.left),dfs(node.right))+1

            return depth


        return dfs(root)-1
