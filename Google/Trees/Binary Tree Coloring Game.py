Binary Tree Coloring Game# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        
        def get_the_red_node(node):
            
            if not node:
                return None
            
            if node.val == x:
                return node
            
            left = get_the_red_node(node.left)
                
            right = get_the_red_node(node.right)
            
            return left if left else right
        
        
        
        def find_total_red_node_below(node):
            if not node:
                return 0
            
            left = find_total_red_node_below(node.left)
            right = find_total_red_node_below(node.right)
            
            return left+right+1
        
        red_node_root = get_the_red_node(root)

        left_subtree_nodes = find_total_red_node_below(red_node_root.left)

        right_subtree_nodes = find_total_red_node_below(red_node_root.right)

        parent_node_nodes = n-(left_subtree_nodes+right_subtree_nodes+1)

        
        

        return (left_subtree_nodes+right_subtree_nodes)<parent_node_nodes or (left_subtree_nodes+parent_node_nodes)<right_subtree_nodes or (right_subtree_nodes+parent_node_nodes)<left_subtree_nodes
            
            
                
        
        
        
        
        
        
            
        
            
        
