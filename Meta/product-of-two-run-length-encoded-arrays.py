class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        

        v1=v2=f1=f2=i=j = 0

        m,n = len(encoded1),len(encoded2)
        
        ans = []

        while i<m or j<n:
            if f1==0 and i<m:
                v1,f1 = encoded1[i]
            if f2 ==0 and j<n:
                v2,f2 = encoded2[j]
            
            curr_min, product = min(f1,f2), v1 * v2

            if ans and ans[-1][0] == product:
                ans[-1][1] += curr_min
            else:
                ans.append([product,curr_min])
            
            f1-=curr_min
            f2-=curr_min
            
            if f1==0:
                i+=1
            if f2==0:
                j+=1
            

        return ans
            


