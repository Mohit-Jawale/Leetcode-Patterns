#### this question is very interesting and has appering in Amazon OA multiple times

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        N = len(s)
        prefixSum = [0]* N
        leftbracket = [-1] * N
        rightbracket = [N+1] * N

        for i in range(N):
            if s[i]=='|':
                leftbracket[i] = i
            else:
                if i>0:
                    leftbracket[i]=leftbracket[i-1]
        
        for i in reversed(range(N)):
            if s[i]=='|':
                rightbracket[i] = i
            else:
                if i<(N-1):
                    rightbracket[i] = rightbracket[i+1]

        for i in range(N):
            if s[i]=='*':
                prefixSum[i] = prefixSum[i-1]+1 if i>0 else 1
            else:
                if i>0:
                    prefixSum[i]=prefixSum[i-1]
        
        ans = []
        for left,right in queries:

            rightmost = rightbracket[left]
            leftmost = leftbracket[right]

            if leftmost>rightmost:
                ans.append(prefixSum[leftmost] - prefixSum[rightmost])
            else:
                ans.append(0)
                
        return ans



        
        
        

