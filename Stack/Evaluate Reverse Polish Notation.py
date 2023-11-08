class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                if stack:
                    right = stack.pop()
                if stack:
                    left = stack.pop()

                ans = int (eval("left"+token+"right")) 
                stack.append(ans)

        return stack[0]           
