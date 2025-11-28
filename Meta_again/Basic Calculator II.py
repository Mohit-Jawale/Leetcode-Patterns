class Solution:
    def calculate(self, s: str) -> int:

        curr=prev=res = 0

        current_op = '+'

        i = 0

        while i<len(s):

            if s[i].isdigit():

                while i<len(s) and s[i].isdigit():
                    curr = curr*10 + int(s[i])
                    i+=1
                
                if current_op == '+':

                    res+=curr
                    prev = curr

                elif current_op == '-':

                    res-=curr
                    prev = -curr  ### careful here as u can forget to add - sign

                elif current_op == '*':
                    res-=prev
                    res+=prev*curr
                    prev = prev*curr

                elif current_op == '/':
                    res-=prev
                    res+=int(prev/curr)
                    prev = int(prev/curr)

                curr = 0

            elif s[i]!=" ":
                current_op = s[i]
                i+=1
            else:
                i+=1 ### this is imp for the case where there are spaces

        return res

                



        
