class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        stack = []


        for index,char in enumerate(s):

            if char in ['(',')']:

                if char == '(':
                    stack.append(('(',index)) 
                elif char == ')':
                    if stack and stack[-1][0]=='(':
                        stack.pop()
                    else:
                        stack.append((')',index))
        

        ans = ""
        n = len(s)
        for index,char in enumerate(s[::-1]):
            
            if stack and stack[-1][1] == (n-index-1):
                stack.pop()
                continue
            ans+=char
     
        return ans[::-1]
