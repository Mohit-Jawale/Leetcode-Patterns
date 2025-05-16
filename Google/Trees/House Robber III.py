# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:



        def max_rob_money(node):

            if not node:
                return (0,0)


            left_take,left_not_take = max_rob_money(node.left)
            right_take,right_not_take = max_rob_money(node.right)

            rob_this = node.val+left_not_take+right_not_take
            not_rob_this = max(left_take+right_not_take,right_take+left_not_take,right_take+left_take,left_not_take+right_not_take)

            return (rob_this,not_rob_this)

            
        return max(max_rob_money(root))














# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}

        def max_rob_money(node,canRob):

            if not node:
                return 0
            if (node,canRob) in memo:
                return memo[(node,canRob)]
            
            if canRob:
                left_total_money = max_rob_money(node.left,False)
                right_total_money = max_rob_money(node.right,False)
                memo[(node,canRob)] = left_total_money+right_total_money+node.val
                return left_total_money+right_total_money+node.val

            else:

                take_left = max_rob_money(node.left,True)
                take_right = max_rob_money(node.right,True)

                dont_take_right = max_rob_money(node.right,False)

                dont_take_left = max_rob_money(node.left,False)

                memo[(node,canRob)] = max(take_left+take_right,take_left+dont_take_right,take_right+dont_take_left,dont_take_right+dont_take_left)
                
                return max(take_left+take_right,take_left+dont_take_right,take_right+dont_take_left,dont_take_right+dont_take_left)
        

        return max(max_rob_money(root,True),max_rob_money(root,False))


            
