# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

   
        def dfs(inorder,postorder):

            if len(inorder)==1:
                if inorder[0]==postorder[-1]:
                    postorder.pop()
                return TreeNode(inorder[0])
            
            root = postorder.pop()
            rootidx = inorder.index(root)
            right = None
            if rootidx+1<len(inorder):
                right = dfs(inorder[rootidx+1:],postorder)
            left = None
            if rootidx>0:
                left = dfs(inorder[:rootidx],postorder)

            node = TreeNode(root)
            if left:
                node.left = left
            if right:
                node.right = right

            return node
        
        return dfs(inorder,postorder)



        
