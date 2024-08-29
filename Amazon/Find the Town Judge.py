class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        inward = collections.defaultdict(list)
        outward = collections.defaultdict(list)

        for i ,j in trust:

            inward[j].append(i)
            outward[i].append(j)

        ans = []
        for i in range(1,n+1):
            if len(inward[i])==n-1 and i not in outward:
                ans.append(i)

        return -1 if len(ans)!=1 else ans[0]
        
