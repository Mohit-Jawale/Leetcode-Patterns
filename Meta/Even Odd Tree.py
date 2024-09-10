# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:


        ## even index-> odd int -> in incre
        ### odd index -> even int -> des

        queue = deque([[root]])
        ans = [[root.val]]
        level = 0

        while queue:

            levels = queue.popleft()

            temp = []
            temp_ans = []

            for node in levels:
                if node.left:
                    temp.append(node.left)
                    temp_ans.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    temp_ans.append(node.right.val)
            
            if temp:
                queue.append(temp)
                ans.append(temp_ans)
        
        
        for index,values in enumerate(ans):

            if index%2==0:### even
                prev = -float('inf')
                for num in values:
                    if num%2==0:
                        return False
                    if prev>=num:
                        return False
                    prev = num
            else:### odd
                prev = float('inf')
                for num in values:
                    if num%2!=0:
                        return False
                    if prev<=num:
                        return False

                    prev = num
        return True

                    
                

           

        
        
            
        
        
