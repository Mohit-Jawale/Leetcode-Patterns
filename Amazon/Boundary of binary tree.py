# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        leafNode = []
        leftboundary = []
        rightboundary = []

        def findleaf(node):

            if not node:
                return
            
            if root!=node and (not node.left and not node.right):
                leafNode.append(node.val)

            findleaf(node.left)
            findleaf(node.right)
        
        def findleftboundary(node):
            if not node:
                return

            if not ( not node.left and not node.right) and node.left:
                leftboundary.append(node.val)
                findleftboundary(node.left)
            elif not (not node.left and not node.right) and not node.left:
                  leftboundary.append(node.val)
                  findleftboundary(node.right)
                
         
        def findrightboundary(node):
            if not node:
                return

            if not ( not node.left and not node.right) and node.right:
                rightboundary.append(node.val)
                findrightboundary(node.right)
            elif not (not node.left and not node.right) and not node.right:
                  rightboundary.append(node.val)
                  findrightboundary(node.left)
                

        findleaf(root)
        findleftboundary(root.left)
        findrightboundary(root.right)
        
        return([root.val]+leftboundary+leafNode+rightboundary[::-1])

        
