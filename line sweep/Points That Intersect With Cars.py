class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        

        line = [0]* 102

        for s,e in nums:
            line[s]+=1
            line[e+1]-=1
        
        count = 0
        ans = 0
        for i in range(102):

            count+=line[i]

            if count>0:
                ans+=1
        
        return ans

