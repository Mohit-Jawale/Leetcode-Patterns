# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

            
      
        def removeRedundantNode(node):
            if not node:
                return
            if node.val>=low and node.val<=high:
                node.left = removeRedundantNode(node.left)
                node.right = removeRedundantNode(node.right)
            else:
                if node.val<low:
                    return removeRedundantNode(node.right)
                elif node.val>high:
                    return removeRedundantNode(node.left)
                else:
                    return None
            return node

        return removeRedundantNode(root)
