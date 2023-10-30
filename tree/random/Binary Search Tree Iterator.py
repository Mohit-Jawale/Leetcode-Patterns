# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.head = TreeNode(-1)
        self.inorder = self.head
        self.dfs(self.root)
        self.inorder = self.head
        
    
    def dfs(self,node):
        if not node:
            return None
    
        self.dfs(node.left)
        self.inorder.right = TreeNode(node.val)
        self.inorder = self.inorder.right
        self.dfs(node.right)

        return

    def next(self) -> int:
        self.inorder = self.inorder.right
        return self.inorder.val
        
        

    def hasNext(self) -> bool:
        if self.inorder.right:
            return True
        else:
            return False    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
