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
        serializedStr = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                serializedStr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serializedStr.append('')
        
        return ",".join(serializedStr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        deserializeStr = data.split(',')
        root = TreeNode(deserializeStr[0])
        queue = collections.deque([root])
        i=1
        while queue:
            node = queue.popleft()
            if i<len(deserializeStr) and deserializeStr[i]:
                node.left = TreeNode(int(deserializeStr[i]))
                queue.append(node.left)
            if i+1<len(deserializeStr) and deserializeStr[i+1]:
                node.right = TreeNode(int(deserializeStr[i+1]))
                queue.append(node.right)
            i+=2
        return root
            
            

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))





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
