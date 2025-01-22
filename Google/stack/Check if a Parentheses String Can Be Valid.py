class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        def checkParentheses(s,locked,op):
            bal,wild = 0,0

            for i in range(len(s)):

                if locked[i]=='1':
                    if op ==s[i]:
                        bal+=1
                    else:
                        bal-=1
                else:
                    wild+=1
                
                if wild+bal<0:
                    return False
            
            return True
        
        if len(s)%2 != 0:
            return False
        
        return checkParentheses(s,locked,'(') and checkParentheses(s[::-1],locked[::-1],')')
                
