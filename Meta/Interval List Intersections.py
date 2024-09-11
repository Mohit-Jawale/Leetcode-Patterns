class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        ### step 1: find if the intervals are overlap
        #### step 2: 



        ans = []
        i,j=0,0

        while i<len(firstList) and j<len(secondList):

            fs,fe = firstList[i]
            ss,se = secondList[j]

            head = max(fs,ss)
            tail = min(fe,se)
            
            if head<=tail:
                ans.append([head,tail])
            
            if fe<se:
                i+=1
            else:
                j+=1
               
        
        return(ans)
            
