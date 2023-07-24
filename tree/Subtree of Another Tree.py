# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        ans = True

        def same_tree(node1,node2):

            nonlocal ans

            if not node1 and not node2:
                return

            if not node1 or not node2:
                ans = False
                return

            if node1.val != node2.val:
                ans = False  

            same_tree(node1.left,node2.left)
            same_tree(node1.right,node2.right)

        
        if not subRoot:
            return True
        if not root:
            return False

        same_tree(root,subRoot)
        if ans == True:
            return ans
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))   

        return False       
                





        
