class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        prefixSum = [0]*(n+1) ### this is diff array technique for range update

        for start,end,direction in shifts:
            if direction == 1:
                x = 1 
                prefixSum[start]+=x
                prefixSum[end+1]-=x
            else:
                x = -1
                prefixSum[start]+=x
                prefixSum[end+1]-=x


        res = []
        for i in range(1,len(prefixSum)):

            prefixSum[i] += prefixSum[i-1]
        

        for i in range(n):
            shifted_char = ((ord(s[i])-97)+prefixSum[i]+26)%26
            res.append(chr(shifted_char+97))
        
        return "".join(res)
        
   

        
