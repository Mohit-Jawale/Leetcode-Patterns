# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        
        ######          1
        ####    2             3
        ## 4       5         6       7
        
        ### parent_stack = [1,1,1,1,1,1,1]
        
        ### 
        
        
        queue = collections.deque([root])
        delete_nodes_set = set(to_delete)
        forest_roots = []
        if root.val not in delete_nodes_set:
            forest_roots.append(root)
        
        while queue:
            
            node = queue.popleft()
            
            if node.val in delete_nodes_set:
                
                if node.left:
                    queue.append(node.left)
                    if node.left.val not in delete_nodes_set:
                        forest_roots.append(node.left)
                    node.left = None
                if node.right:
                    queue.append(node.right)
                    if node.right.val not in delete_nodes_set:
                        forest_roots.append(node.right)
                    node.right = None
            else:
                if node.left:
                    queue.append(node.left)
                    if node.left.val in delete_nodes_set:
                        node.left = None ### backward remove of node
                if node.right:
                    queue.append(node.right)
                    if node.right.val in delete_nodes_set:
                        node.right = None
  
        return forest_roots
