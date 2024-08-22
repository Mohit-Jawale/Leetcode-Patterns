class Solution:
    def simplifyPath(self, path: str) -> str:

  
        stack = ["/"]

        path_list = path.split("/")
        path_list = path_list[1:]
        

        for index,value in enumerate(path_list):
            
            if stack and value == "..":
                if len(stack)>=3:
                    stack.pop()
                    stack.pop()

            elif stack and stack[-1]=='/' and value!='' and value!='.':
                stack.append(value)
                stack.append('/')

        
        if len(stack)>1:
            return("".join(stack[:-1]))
        else:
            return("".join(stack))
            


            
        
