class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ']':'[',
            '}':'{',
            ')':'('
        }


        stack = []
        for bracket in s:
            if bracket in ["(",'{','[']:
                stack.append(bracket)
            else:
                if stack:
                    top = stack.pop()
                    if mapping[bracket]==top:
                        continue
                    else:
                        return False
                else:
                    return False        

        return False if stack else True                       
        
