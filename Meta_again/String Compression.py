class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars)==1:
            return 1
        ### edge cases
        ### [a],[a,b],[a,a]

        left,right = 0,1
        ans_ptr = 0
        chars.append("END")
        chars.append("END")
        N = len(chars)

        while right<N:

            if chars[left]==chars[right]:
                right+=1
            else:
                if right-left<=9 and right-left>1:
                    chars[ans_ptr]=chars[left]
                    ans_ptr+=1
                    chars[ans_ptr] = str(right-left)
                    ans_ptr+=1
                elif right-left>9:
                    chars[ans_ptr]=chars[left]
                    ans_ptr+=1
                    num = str(right-left)
                    for i in num:
                        chars[ans_ptr]=i
                        ans_ptr+=1
                elif right-left==1:
                    chars[ans_ptr]=chars[left]
                    ans_ptr+=1
                left = right
  
        return ans_ptr















        
