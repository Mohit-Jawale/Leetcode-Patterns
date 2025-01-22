class Solution:
    def checkValidString(self, s: str) -> bool:


        def checkParenthesis(s,op):

            bal,wild = 0, 0 

            for i in range(len(s)):

                if s[i] in ['(',')']:
                    if s[i]==op:
                        bal+=1
                    else:
                        bal-=1
                
                if s[i]=='*':
                    wild+=1
                
                if bal+wild<0:
                    return False
            
            return True
        
        return checkParenthesis(s,'(') and checkParenthesis(s[::-1],')')
                
                
        
