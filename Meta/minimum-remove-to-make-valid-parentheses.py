class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        stack = []

        map = {')':'('}

        for index,i in enumerate(s):
            
            if (ord(i)-ord('a'))>=0 and (ord(i)-ord('a'))<=25:
                continue
            else:
                if i == '(':
                    stack.append((i,index))
                elif stack and stack[-1][0] == map[i]:
                    stack.pop()
                else:
                    stack.append((i,index))
        
        while stack:
            index = stack.pop()[1]
            s = s[:index]+s[index+1:]
            
        return s

