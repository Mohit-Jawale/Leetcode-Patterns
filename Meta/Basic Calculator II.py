class Solution:
    def calculate(self, s: str) -> int:

        cur = prev = res = 0
        current_op = '+'
        i = 0

        while i<len(s):

            if s[i].isdigit():
                print(res,current_op)
                while i<len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i+=1
                i-=1
               
                if current_op == '+':
                    res+=cur

                    prev = cur
                elif current_op == '-':
                    res-=cur

                    prev = -cur
                elif current_op =='*':

                    res-=prev
                    res+= prev*cur

                    prev = cur*prev
                elif current_op == '/':

                    res-=prev
                    res += int(prev/cur)

                    prev = int(prev/cur)
                
                cur = 0

            elif s[i] != " " :
                current_op = s[i]
            
            i+=1
        return res



                
        
