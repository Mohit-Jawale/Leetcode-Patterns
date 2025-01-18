class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        

        n = len(values)
        prefix_max = [0]*n
        prefix_max[0] = values[0] + 0

        for i in range(1,n):
            prefix_max[i] = max(prefix_max[i-1],values[i]+i)

        max_score = 0
        for j in range(1,n):

            score = prefix_max[j-1] + values[j]-j

            max_score = max(score,max_score)
        

        return max_score
            

        



