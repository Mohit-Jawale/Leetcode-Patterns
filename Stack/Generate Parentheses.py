class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        open_bracket = '('
        close_bracket = ')'

        def check_parenthesis(s):
            stack = []
            for i in s:
                if i == open_bracket:
                    stack.append(i)
                else:
                    if stack and stack[-1]==open_bracket:
                        stack.pop()
                    else:
                        return False
            return True if len(stack)==0 else False
        
        ans = []
        def dfs(s):

            if len(s)==n*2:
                if check_parenthesis(s):
                    ans.append(copy.deepcopy(s))
                return
            
            for i in ['()',')(','((','))']:
                s = list(s)
                middle = len(s)//2
                front = s[:middle]
                end = s[middle:]
                newStr = "".join(front+list(i)+end)
                dfs(newStr)
        dfs('()')
        return ans


        

        
