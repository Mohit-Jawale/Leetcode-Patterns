# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        lookup = {0:1}
        count = 0
        def dfs(node,total):

            nonlocal lookup,count
            if not node:
                return
                
            total+=node.val

            count+= lookup.get(total-targetSum,0)
            
            lookup[total] = lookup.get(total,0)+1

            dfs(node.left,total)
            dfs(node.right,total)

            lookup[total]-=1

        dfs(root,0)
        return count

        
