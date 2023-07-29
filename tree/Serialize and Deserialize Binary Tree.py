# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                ans.append("N")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return    
        dfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if data[i]=='N':
                i+=1
                return
            node = TreeNode(int(data[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
               
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
