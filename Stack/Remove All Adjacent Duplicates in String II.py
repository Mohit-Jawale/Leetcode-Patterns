class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
     
        stack = [('#',0)]

        for i in range(len(s)):
            
            if stack[-1][0]==s[i]:
                    char,cnt = stack.pop()
                    stack.append((char,cnt+1))
                    if stack[-1][1]==k:
                        stack.pop()       
            else:
                stack.append((s[i],1))
                    
        ans = [i[0]*c for i,c in stack]
        return "".join(ans)
        




        
