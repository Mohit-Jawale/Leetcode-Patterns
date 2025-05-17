# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def findLCA(node):

            if not node:
                return None
            
            if p.val == node.val or q.val == node.val:
                return node
            
            isLCAOnLeft = findLCA(node.left)
            isLCAOnRight = findLCA(node.right)

            if isLCAOnLeft and isLCAOnRight:
                return node
            if isLCAOnRight and not isLCAOnLeft:
                return isLCAOnRight
            if not isLCAOnRight and isLCAOnLeft:
                return isLCAOnLeft
            return None
        
        return findLCA(root)

            
            
            

        
